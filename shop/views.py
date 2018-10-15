from django.views import View
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse_lazy
from django.core.mail import mail_admins

from shop.models import Product
from . import forms

class ProductListView(View):

    page_template_name = 'shop/shop.html'
    list_template_name = 'shop/shop_list.html'
    ajax_parametr = 'page'
    content = {}
    paginate_by = 12
    is_show_more = True
    start_page_num = 1

    def get_product_list(self, page_num):

        all_products = list(Product.objects.all())
        paginator = Paginator(all_products, self.paginate_by)
        self.is_show_more = False if page_num >= paginator.num_pages else True
        return paginator.page(page_num).object_list

    def get(self, request):

        if self.ajax_parametr in request.GET:
            print(request.GET)
            self.content['prod_list']= self.get_product_list(int(request.GET.get('page')))
            self.content['is_show_more'] = self.is_show_more
            return render(request, self.list_template_name, self.content)

        else:
            self.content['prod_list'] = self.get_product_list(self.start_page_num)
            self.content['is_show_more'] = self.is_show_more
            return render(request, self.page_template_name, self.content)



class ProductDetailView(DetailView):

    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = forms.OrderForm();
        form.fields['product_id'].initial = self.kwargs['pk']
        form.fields['product_name'].initial= Product.objects.only('product_name').get(pk=self.kwargs['pk']).product_name
        context['form'] = form 
        return context

    def post(self, request, **kwargs):

        success = reverse_lazy('shop:success')
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print('*'*100)
            print(form)
            send_message(form)
            return redirect(success)

def oreder_success(request):
    
    return render(request, 'shop/success.html')

def send_message(form):

    subject = 'Subject'
    html_message = render_to_string('shop/mail_template.html', {'context': form})
    plain_message = strip_tags(html_message)
    from_email = 'From <from@example.com>'

    mail_admins(subject, plain_message, from_email, html_message=html_message)
