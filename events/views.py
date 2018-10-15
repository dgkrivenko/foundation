from django.shortcuts import render
from django.views.generic import TemplateView

from . import models

class EventsView(TemplateView):

    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['content'] = models.Event.objects.all()
        print(context['content'])
        return context




   