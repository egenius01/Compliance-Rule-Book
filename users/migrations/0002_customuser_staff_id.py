# Generated by Django 2.2.7 on 2019-12-19 01:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='staff_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=6),
            preserve_default=False,
        ),
    ]
