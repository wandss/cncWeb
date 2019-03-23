from uuid import uuid4
from django.db import models
from motor.models import Motor
from rpi.models import RpiBoard


class Gcode(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    gcode_file = models.FileField(upload_to="media")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.gcode_file.name)


class Settings(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    project_name = models.CharField(max_length=30)
    motor = models.ManyToManyField(Motor)
    pi_board = models.ForeignKey(RpiBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

"""
TODO:
    Change associations.
    A board has motors connected to its pins.
    The the project will be associated with board only
    Remove motor attribute from plot.models.Settings
"""
