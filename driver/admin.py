from django.contrib import admin
from .models import Driver

# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display= (
                'name_of_driver',
                'uploadedImage',
                'date_added',
                'date_updated')
admin.site.register(Driver,DriverAdmin)