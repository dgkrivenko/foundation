from django.contrib import admin

from shop.models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ['product_name', 'product_id', 'user_email', 'user_name', 'user_phone', 'user_address', 'user_add_info']
    list_display = ['user_name', 'product_id', 'product_name', 'created_at']

    def has_add_permission(self, request, obj=None):
        return False

    def format_date(self, obj):
        return obj.date.strftime('%d-%m-%Y %H:%M:S')