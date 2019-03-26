from django.contrib import admin
from .models import RpiBoard, RpiPinOut, Connection


class RpiPinOutAdmin(admin.ModelAdmin):
    list_display = ['number', 'function', 'bcm_number']

admin.site.register(RpiBoard)
admin.site.register(RpiPinOut, RpiPinOutAdmin)
admin.site.register(Connection)
