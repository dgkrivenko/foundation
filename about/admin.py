from django.contrib import admin

from . import models

@admin.register(models.Founder)
class FounderAdmin(admin.ModelAdmin):

    list_display = ['name']

    def has_add_permission(self, request):

        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(models.Foundation)
class FoundationAdmin(admin.ModelAdmin):

    list_display = ['detail_page_title']

    def has_add_permission(self, request):
        
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(models.Directors)
class DirectorAdmin(admin.ModelAdmin):

    list_display = ['name', 'status']