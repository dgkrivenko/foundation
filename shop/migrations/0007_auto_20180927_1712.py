# Generated by Django 2.1 on 2018-09-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180927_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, verbose_name='Product name'),
        ),
    ]
