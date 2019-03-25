from uuid import uuid4
from django.db import models
from rpi.models import RpiBoard


class Gcode(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    gcode_file = models.FileField(upload_to="media")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.gcode_file.name)


class Plot(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    board = models.ForeignKey(RpiBoard, on_delete=models.CASCADE, null=True,
                              blank=True)


"""
TODO:
    Change associations.
    A board has motors connected to its pins.
    The project will be associated with board only
    Remove motor attribute from plot.models.Settings
"""
