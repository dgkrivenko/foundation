"""foundation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include


from mainapp import urls as mainapp_urls
from shop import urls as shop_urls
from contacts import urls as contacts_urls
from events import urls as events_urls
from about import urls as about_urls
from apply import urls as apply_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(mainapp_urls)),
    path('shop/', include(shop_urls)),
    path('contacts/', include(contacts_urls)),
    path('events/', include(events_urls)),
    path('about/', include(about_urls)),
    path('apply/', include(apply_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
