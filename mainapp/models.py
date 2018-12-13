from django.db import models


class Story(models.Model):

    class Meta:
        verbose_name_plural = "Stories"

    title = models.CharField(verbose_name="Title", max_length=100)
    img = models.ImageField(verbose_name="Image", upload_to='news_img', blank=True)
    description = models.TextField(verbose_name="Description")
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' - '.join((self.title, str(self.published_on)))


class Banner(models.Model):

    banner_img = models.ImageField(verbose_name="Banner image", upload_to='banner_img', blank=True)
    banner_title = models.CharField(verbose_name="Banner title", max_length=100)
    banner_date = models.CharField(verbose_name="Date", max_length=100)

    def __str__(self):
        return self.banner_title