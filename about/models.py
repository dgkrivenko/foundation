from django.db import models

class Founder(models.Model):

    class Meta:
        verbose_name_plural = "Founder"

    name = models.CharField(verbose_name='Name', max_length=100)
    short_description = models.TextField(verbose_name='Short description')
    full_description = models.TextField(verbose_name='Full description')
    detail_page_title = models.CharField(verbose_name='Detail page title', max_length=100)
    img = models.ImageField(verbose_name="Image", upload_to='about_img', blank=True)

    def __str__(self):

        return self.name

class Foundation(models.Model):

    class Meta:
        verbose_name_plural = "Foundation"

    short_description = models.TextField(verbose_name='Short description')
    full_description = models.TextField(verbose_name='Full description')
    detail_page_title = models.CharField(verbose_name='Detail page title', max_length=100)

    def __str__(self):

        return 'Foundation'

class Directors(models.Model):
    
    class Meta:
        verbose_name_plural = "Directors"

    name = models.CharField(verbose_name='Name', max_length=100)
    status = models.CharField(verbose_name='Status', max_length=100)
    img = models.ImageField(verbose_name="Image", upload_to='about_img', blank=True)
    short_description = models.TextField(verbose_name='Short description')
    full_description = models.TextField(verbose_name='Full description')
    detail_page_title = models.CharField(verbose_name='Detail page title', max_length=100)

    def __str__(self):

        return self.name
