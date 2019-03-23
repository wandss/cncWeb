from django.contrib import admin
from .models import RpiBoard, RpiPinOut


class RpiPinOutAdmin(admin.ModelAdmin):
    list_display = ['number', 'function', 'bcm_number']

admin.site.register(RpiBoard)
admin.site.register(RpiPinOut, RpiPinOutAdmin)
