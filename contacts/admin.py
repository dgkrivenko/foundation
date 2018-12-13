from django.contrib import admin
from . import models


@admin.register(models.PersonContact)
class PersonContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


@admin.register(models.CompanyContact)
class CompanyContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'email', 'phone']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(models.Bank)
class CompanyContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'bic', 'ban']
