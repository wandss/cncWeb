from uuid import uuid4
from django.db import models


class Gcode(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    gcode_file = models.FileField(upload_to="media")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.gcode_file.name)


class RpiConfig(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    motor_type = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    # TODO: add Pins number/name
