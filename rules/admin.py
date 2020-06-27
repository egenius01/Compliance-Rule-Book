from django.contrib import admin
from .models import Authority
from .models import Frequency
from .models import MasterRuleBook
from .models import Sources,TeamLead
from .models import Category
from .models import Upload
from .models import Process
import csv
#Register your models here.
admin.site.register(Authority)
admin.site.site_header = 'Compliance RuleBook Admin'


@admin.register(Frequency)
class Frequency (admin.ModelAdmin):
    icon_name = 'autorenew'

@admin.register(Sources)
class Sources(admin.ModelAdmin):
    icon_name = 'bubble_chart'

@admin.register(Category)
class Category (admin.ModelAdmin):
    icon_name = 'dashboard'

@admin.register(Process)
class Process(admin.ModelAdmin):
    icon_name = 'donut_small'



@admin.register(MasterRuleBook)
class MasterRuleBookAdmin(admin.ModelAdmin):
    icon_name = 'assignment_return'
    list_display = ('returns','owner','section','frequency','authority','lead_days','initial_date_of_rendition','department')
    list_filter = ('returns','authority','frequency','initial_date_of_rendition','lead_days','department', 'owner')
    ordering = ('owner','returns','frequency','department')


@admin.register(Upload)
class Upload (admin.ModelAdmin):
    icon_name = 'publish'
    list_display = ('returns','approved','published_date')
    list_filter = ('approved','returns','published_date')
    ordering = ('approved','published_date','returns')
    fieldsets = [
        ('Approve Upload',{'fields':["approved"]}),
         ('image',{'fields':["images"]}),
        ("description",{'fields':["description"]}),
        ('posted_by',{'fields':["posted_by"]})
    ]
    readonly_fields = ["images","description","posted_by"]

@admin.register(TeamLead)
class TeamLead (admin.ModelAdmin):
    icon_name = 'person_pin'
    list_display = ('name','department')
    list_filter = ('department','name')
    ordering = ('department','name')
