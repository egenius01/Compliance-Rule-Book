from django.contrib.admin import ModelAdmin, site


from django.contrib.auth.models import Group

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser, Department

# Register your models here.



class CustomUserAdmin(UserAdmin):
    icon_name = 'person'
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email','username','is_staff','staff_id','department'] # new

site.register(CustomUser, CustomUserAdmin, )
site.register(Department)

site.unregister(Group)