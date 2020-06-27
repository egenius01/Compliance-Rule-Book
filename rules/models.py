from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime, timedelta, date
from django.utils import timezone
from users.models import CustomUser, Department

# Create your models here.

class Authority(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authorities'

class Process(models.Model):
    process = models.CharField(max_length=60)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Processes'

class Frequency(models.Model):
    frequency = models.CharField(max_length=5)
    description = models.CharField(max_length=30, help_text='e.g Daily, Weekly, Biennial, Periodically e.t.c')
    multiplier = models.PositiveIntegerField()
    refkey = str(frequency) + str(multiplier)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Frequencies'


class Category(models.Model):
    name = models.CharField(max_length=128,null=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'



class Sources(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    source = models.CharField(max_length=250, null=False)
    def __str__(self):
        return self.source

    class Meta:
        verbose_name_plural = 'Sources'

class TeamLead(models.Model):
    name  = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
class MasterRuleBook(models.Model):
    returns = models.CharField(max_length=200, null=False)
    section = models.CharField(max_length= 200, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', default=1, on_delete=models.CASCADE)
    with_returns = models.BooleanField(default = True)
    frequency = models.ForeignKey('Frequency',on_delete=models.CASCADE, null = True ,blank=True)
    authority = models.ForeignKey('Authority', on_delete=models.CASCADE,)
    Responsible_Officer = models.ForeignKey(
        get_user_model(),on_delete=models.CASCADE
    )
    owner =  models.ForeignKey(
        'TeamLead', on_delete=models.CASCADE
    )
    circular_name = models.CharField(max_length=350)
    circular = models.FileField(upload_to='upload/files/circular/')
    lead_days = models.PositiveIntegerField(null = True ,blank=True)
    initial_date_of_rendition = models.DateTimeField(null = True ,blank=True)
    sanctions = models.CharField(max_length=200, default="Shall Attract Appropriate Sanctions")
    def __str__(self):
        return (self.returns)

    def next_rendition_date(self):
        return self.initial_date_of_rendition + timedelta(days=self.lead_days)

    def get_absolute_url(self):
        return reverse('rule_view', kwargs={
            'id':self.id
        })


class Upload(models.Model):
    returns = models.ForeignKey(MasterRuleBook, on_delete=models.CASCADE)
    images = models.FileField(upload_to='upload/files/')
    description = models.TextField(max_length=1000)
    approved = models.BooleanField(default = False)
    published_date = models.DateTimeField(blank=False, auto_now=True,)
    owner = models.CharField(max_length=100, default = 1)
    posted_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            return "Photo <%s:%s>" % (self.title, public_id)
    def __str__(self):
        a = str(self.published_date)
        return ("New Publish on " + a + "by" + "")
    def get_absolute_url(self):
        return reverse("rules:upload_list", kwargs={"id":self.id})





# class RuleBook(models.Model):
#     returns = models.CharField(max_length=200, null=False)
#     section = models.CharField(max_length=200, null=False)
#     frequency = models.ForeignKey('Frequency', on_delete=models.CASCADE, null=False)
#     authority = models.ForeignKey('Authority', on_delete=models.CASCADE, null=False)
#     Responsible_Officer = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
#     )
#     circular_name = models.CharField(max_length=350)
#     circular = models.FileField(upload_to='upload/files/circular/')




# class MasterRuleBook(models.Model):
#     returns = models.CharField(max_length=200, null=False)
#     section = models.CharField(max_length= 200, null=False)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     frequency = models.ForeignKey('Frequency',on_delete=models.CASCADE, null=False)
#     authority = models.ForeignKey('Authority', on_delete=models.CASCADE, null=False)
#     Responsible_Officer = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
#     )
#     circular_name = models.CharField(max_length=350)
#     circular = models.FileField(upload_to='upload/files/circular/')
#     lead_days = models.PositiveIntegerField()
#     initial_date_of_rendition = models.DateField()
#     def next_rendition_date(self):
#         return self.initial_date_of_rendition + timedelta(days=self.lead_days)
#
#
#     def __str__(self):
#         return (self.returns)
#
#     def get_absolute_url(self):
#         return reverse('rule_view', kwargs={
#             'id':self.id
