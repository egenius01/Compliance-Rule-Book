from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    staff_id = models.CharField(max_length=6)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)