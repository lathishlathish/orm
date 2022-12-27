from django.db import models
from django.contrib import admin

# Create your models here.
class Employee (models.Model):
    employeeid=models.CharField(primary_key=True,max_length=20,help_text="employeeid")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    role=models.CharField(max_length=20)
    salary=models.IntegerField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('employeeid','name','age','email','role','salary')