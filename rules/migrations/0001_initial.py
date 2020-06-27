# Generated by Django 2.2.7 on 2020-01-03 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_customuser_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(max_length=5)),
                ('description', models.CharField(help_text='e.g Daily, Weekly, Biennial, Periodically e.t.c', max_length=30)),
                ('multiplier', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MasterRuleBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returns', models.CharField(max_length=200)),
                ('section', models.CharField(max_length=200)),
                ('with_returns', models.BooleanField(default=True)),
                ('circular_name', models.CharField(max_length=350)),
                ('circular', models.FileField(upload_to='upload/files/circular/')),
                ('lead_days', models.PositiveIntegerField(blank=True, null=True)),
                ('initial_date_of_rendition', models.DateField(blank=True, null=True)),
                ('Responsible_Officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('authority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Authority')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Department')),
                ('frequency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rules.Frequency')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='upload/files/')),
                ('description', models.TextField(max_length=1000)),
                ('approved', models.BooleanField(default=False)),
                ('published_date', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('returns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.MasterRuleBook')),
            ],
        ),
        migrations.CreateModel(
            name='TeamLead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Department')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Department')),
            ],
        ),
        migrations.AddField(
            model_name='masterrulebook',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.TeamLead'),
        ),
    ]
