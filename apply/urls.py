from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apply.views import ApplyView

app_name = 'apply'

urlpatterns = [
    path('', ApplyView.as_view(), name='apply_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
