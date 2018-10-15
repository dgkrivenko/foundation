from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.http import request

from . import views

app_name = 'about'

urlpatterns = [
    path('', views.AboutView.as_view(), name='about_main'),
    path('<int:pk>', views.AboutDetailView.as_view(), name='about_detail'),
    path('founder/', views.founder_detail, name='founder_detail'),
    path('foundation/', views.foundation_detail, name='foundation_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
