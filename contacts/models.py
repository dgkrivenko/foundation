from django.db import models


class CompanyContact(models.Model):
    address = models.CharField(verbose_name="Address", max_length=100)
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(verbose_name="Phone", max_length=100)

    def __str__(self):
        return self.name


class PersonContact(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(verbose_name="Phone", max_length=100)

    def __str__(self):
        return self.name


class Bank(models.Model):
    name = models.CharField(verbose_name="Bank name", max_length=100)
    bic = models.CharField(verbose_name="BIC", max_length=100)
    ban = models.CharField(verbose_name="BAN", max_length=100)
    currency = models.CharField(verbose_name="Сurrency", max_length=100)

    def __str__(self):
        return self.name


