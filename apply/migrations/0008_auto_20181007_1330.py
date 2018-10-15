# Generated by Django 2.1 on 2018-10-07 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0007_auto_20181007_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='participant',
        ),
        migrations.AddField(
            model_name='participant',
            name='prize',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apply.Prize'),
            preserve_default=False,
        ),
    ]
