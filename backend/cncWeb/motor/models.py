from uuid import uuid4
from django.db import models

# CREATE MOTOR TYPE OPTIONS OR CREATE CLASS
class Motor(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    #motor_type =
    pin_numbers = models.CharField(max_length=20)
    isActive = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
