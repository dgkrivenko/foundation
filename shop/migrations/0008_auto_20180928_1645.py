# Generated by Django 2.1 on 2018-09-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180927_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_add_info',
            field=models.TextField(blank=True, verbose_name='Additional information'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_email',
            field=models.CharField(blank=True, max_length=100, verbose_name='User e-mail'),
        ),
    ]
