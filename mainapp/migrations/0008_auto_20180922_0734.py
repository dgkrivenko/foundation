# Generated by Django 2.1 on 2018-09-22 07:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_story_published_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='banner_name',
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_date',
            field=models.CharField(default=1, max_length=100, verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Banner title'),
            preserve_default=False,
        ),
    ]