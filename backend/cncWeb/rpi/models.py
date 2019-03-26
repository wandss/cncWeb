from uuid import uuid4
from django.db import models
from device.models import Device


class RpiPinOut(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # board = models.ForeignKey(RpiBoard, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(unique=True,
                                         choices=[(i, i) for i in range(1, 41)]
                                         )
    function = models.CharField(max_length=20)
    bcm_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        ordering = ('number',)


class RpiBoard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    available_pins = models.ManyToManyField(RpiPinOut)
    connected_devices = models.ManyToManyField(Device, through="Connection")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Connection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    board = models.ForeignKey(RpiBoard, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    used_pins = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.board, self.device)

    class Meta:
        unique_together = ('device', 'used_pins')

# TODO: REVIEW MODELS
