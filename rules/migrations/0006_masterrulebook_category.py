# Generated by Django 2.2.7 on 2020-01-03 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0005_auto_20200103_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterrulebook',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rules.Category'),
        ),
    ]
