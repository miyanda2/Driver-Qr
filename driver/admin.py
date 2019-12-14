from django.contrib import admin
from .models import Driver,FieldNumber

# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display= (
                'name_of_driver',
                'uploadedImage',
                'date_added',
                'date_updated')

class DriverFieldNumberAdmin(admin.ModelAdmin):
    list_display = (
        'driver',
        'state_of_issuance',
        'class_of_liscense',
        'number_of_replacement',
        'license_of_number',
        'chassess_number',
        'plate_number',
        'expiry_date',
        'flag',
        'date_added',
        'date_updated'
    )
admin.site.register(Driver,DriverAdmin)
admin.site.register(FieldNumber,DriverFieldNumberAdmin)
