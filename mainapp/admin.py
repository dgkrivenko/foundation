from django.contrib import admin

from mainapp.models import Story
from mainapp.models import Banner

MAX_BANNER_NUM = 3


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['banner_title', 'banner_date']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= MAX_BANNER_NUM:
            return False
        else:
            return True


@admin.register(Story)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_on']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= MAX_BANNER_NUM:
            return False
        else:
            return True
