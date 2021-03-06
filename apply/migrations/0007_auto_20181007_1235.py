# Generated by Django 2.1 on 2018-10-07 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0006_auto_20181007_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100, verbose_name='File name')),
                ('docs', models.FileField(upload_to='docs/')),
            ],
        ),
        migrations.RemoveField(
            model_name='prize',
            name='docs',
        ),
        migrations.AddField(
            model_name='files',
            name='prize',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apply.Prize'),
        ),
    ]
