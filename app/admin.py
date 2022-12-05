from django.contrib import admin
from .models import Costumers


# Register your models here.

class CostumersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'date_create')
