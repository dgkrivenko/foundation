from django.db import models


class Product(models.Model):
    product_name = models.CharField(verbose_name="Product name", max_length=100)
    short_description = models.TextField(verbose_name="Short short_description")
    long_description = models.TextField(verbose_name="Long description")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(verbose_name="Image", upload_to='product_img', blank=True)

    def __str__(self):
        return ' - '.join((self.product_name, str(self.price)))


class Order(models.Model):
    product_name = models.CharField(verbose_name="Product name", max_length=100)
    product_id = models.CharField(verbose_name="Product ID", max_length=100)
    user_name = models.CharField(verbose_name="User name", max_length=100)
    user_email = models.CharField(verbose_name="User e-mail", max_length=100, blank=True)
    user_phone = models.CharField(verbose_name="User phone", max_length=100)
    user_address = models.CharField(verbose_name="User address", max_length=100)
    user_add_info = models.TextField(verbose_name="Additional information", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' - '.join((self.user_name, str(self.created_at.strftime("%Y-%m-%d %H:%M:%S"))))
