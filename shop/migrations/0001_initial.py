# Generated by Django 2.1 on 2018-09-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Title')),
                ('short_description', models.TextField(verbose_name='Short short_description')),
                ('long_description', models.TextField(verbose_name='Long description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.ImageField(blank=True, upload_to='product_img', verbose_name='Image')),
            ],
        ),
    ]
