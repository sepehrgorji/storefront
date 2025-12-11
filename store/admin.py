from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
    
admin.site.register(models.Collection)
admin.site.register(models.Product)
