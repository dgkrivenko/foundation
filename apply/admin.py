from django.contrib import admin
from . import models
from django.template.loader import render_to_string


class FileInline(admin.TabularInline):
    model = models.Files


@admin.register(models.Prize)
class PrizeAdmin(admin.ModelAdmin):
    inlines =[FileInline]

    def get_model_perms(self, request):
        return {}


@admin.register(models.Sport)
class SportContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'prize_category']

    def has_add_permission(self, request):
        return False

    def prize_category(self, obj):
        return render_to_string('apply/prize.html', {'prize': obj.prize})


@admin.register(models.Science)
class SportContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'prize_category']

    def has_add_permission(self, request):
        return False

    def prize_category(self, obj):
        return render_to_string('apply/prize.html', {'prize': obj.prize})


@admin.register(models.Art)
class SportContactAdmin(admin.ModelAdmin):

    list_display = ['name', 'prize_category']
    
    def has_add_permission(self, request):
        return False

    def prize_category(self, obj):
        return render_to_string('apply/prize.html', {'prize': obj.prize})

