from django.urls import path

from mainapp.views import NewsView

app_name = 'mainapp'

urlpatterns = [
    path('', NewsView.as_view(), name='main'),
] 
