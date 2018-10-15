from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views import View

from mainapp.models import Story
from mainapp.models import Banner

class NewsView(View):

    content = {}
    is_show_more = True
    paginate_by = 1
    start_page_num = 1
    ajax_parametr = 'page'
    list_template_name = 'mainapp/news.html'
    page_template_name = 'mainapp/index.html'


    def get_news_list(self, page_num):
        all_news = list(Story.objects.all())
        paginator = Paginator(all_news, self.paginate_by)
        self.is_show_more = False if page_num >= paginator.num_pages else True
        return paginator.page(page_num).object_list
    
    def get(self, request):

        if self.ajax_parametr in request.GET:
            self.content['news_list']= self.get_news_list(int(request.GET.get('page')))
            self.content['is_show_more'] = self.is_show_more
            return render(request, self.list_template_name, self.content)

        else:
            self.content['news_list'] = self.get_news_list(self.start_page_num)
            self.content['is_show_more'] = self.is_show_more
            self.content['banner_slide'] = Banner.objects.all()
            return render(request, self.page_template_name, self.content)

