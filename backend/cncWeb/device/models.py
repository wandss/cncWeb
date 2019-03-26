from uuid import uuid4
from django.db import models


class Device(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=12)
    isActive = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
