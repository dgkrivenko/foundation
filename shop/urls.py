from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shop.views import ProductListView, ProductDetailView, oreder_success

app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('success', oreder_success, name='success')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
