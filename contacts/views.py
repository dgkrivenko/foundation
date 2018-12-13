from django.shortcuts import render
from django.views import View
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import mail_admins

from . import models
from . import forms


class ContactsView(View):
    template_name = 'contacts/contacts.html'
    context = {}

    def get_context_data(self):
        self.context['company_contacts'] = models.CompanyContact.objects.all()
        self.context['persons_contacts'] = models.PersonContact.objects.all()        
        self.context['bank_data'] = models.Bank.objects.all() 
        self.context['form'] = forms.QuestionsFrom()

    def get(self, request):
        self.get_context_data()
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = forms.QuestionsFrom(request.POST)
        send_message(form)
        return render(request, 'contacts/success.html')


def send_message(form):
    subject = 'Subject'
    html_message = render_to_string('contacts/mail_template.html', {'context': form})
    plain_message = strip_tags(html_message)
    from_email = 'From <from@example.com>'
    mail_admins(subject, plain_message, from_email, html_message=html_message)

