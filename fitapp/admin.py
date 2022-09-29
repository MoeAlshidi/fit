from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email'] 

@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display=['id', 'customer', 'image']