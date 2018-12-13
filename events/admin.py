from django.contrib import admin

from . import models


@admin.register(models.Event)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['event_name']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
