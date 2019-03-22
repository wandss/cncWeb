from django.contrib import admin
from .models import RpiBoard, RpiPinOut

admin.site.register(RpiBoard)
admin.site.register(RpiPinOut)
