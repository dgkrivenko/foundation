from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from . import models

class AboutView(TemplateView):

    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['founder'] = models.Founder.objects.all()
        context['foundation'] = models.Foundation.objects.all()
        context['directors'] = models.Directors.objects.all()
        return context

class AboutDetailView(DetailView):

    model = models.Directors
    template_name = 'about/about_detail.html'
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_img'] = True
        return context


def founder_detail(request):

    context = {}
    context['content'] = models.Founder.objects.get()
    context['is_img'] = True
    template_name = 'about/about_detail.html'

    return render(request, template_name, context)

def foundation_detail(request):

    context = {}
    context['is_img'] = False
    template_name = 'about/about_detail.html'
    context['content'] = models.Foundation.objects.all().get()

    return render(request, template_name, context)