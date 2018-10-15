from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
