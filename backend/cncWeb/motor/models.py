from uuid import uuid4
from django.db import models


class MotorType(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Motor(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    motor_type = models.ForeignKey(MotorType, on_delete=models.CASCADE)
    pin_numbers = models.CharField(max_length=20, null=True, blank=True)
    isActive = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.motor_type.name
