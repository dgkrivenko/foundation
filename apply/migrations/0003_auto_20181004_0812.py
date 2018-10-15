# Generated by Django 2.1 on 2018-10-04 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_auto_20181004_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='prize',
        ),
        migrations.AddField(
            model_name='prize',
            name='participant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apply.Participant'),
            preserve_default=False,
        ),
    ]