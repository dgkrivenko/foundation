from django.db import models


class Event(models.Model):
    event_name = models.CharField(verbose_name='Event name', max_length=100)
    ticket_vendor = models.URLField(max_length=200)
    first_screen_top_text = models.TextField(verbose_name="First screen top text", blank=True)
    first_screen_img = models.ImageField(verbose_name="First screen image", upload_to='events_img', blank=True)
    first_screen_bottom_text = models.TextField(verbose_name="First screen bottom text", blank=True)
    second_screen_top_text = models.TextField(verbose_name="Second screen top text", blank=True)
    second_screen_img = models.ImageField(verbose_name="Second screen image", upload_to='events_img', blank=True)
    second_screen_bottom_text = models.TextField(verbose_name="Second screen bottom text", blank=True)
    third_screen_text = models.TextField(verbose_name="Third screen text", blank=True)
    third_screen_img = models.ImageField(verbose_name="Third screen image", upload_to='events_img', blank=True)
    fourth_screen_text = models.TextField(verbose_name="Fourth screen text", blank=True)
    fourth_screen_img = models.ImageField(verbose_name="Fourth screen image", upload_to='events_img', blank=True)

    def __str__(self):
        return self.event_name