from django.contrib import admin
from . models import DataBase

# Register your models here.

# To sort the databases and columns
class sortDB(admin.ModelAdmin):
    list_display = ['status']

# Registering the models

admin.site.register(DataBase)