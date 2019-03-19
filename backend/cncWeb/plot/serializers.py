from rest_framework.serializers import ModelSerializer
from .models import Gcode

class GcodeSerializer(ModelSerializer):

    class Meta:
        model = Gcode
        exclude = ('id',)
