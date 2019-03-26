from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Gcode, Plot

class GcodeSerializer(ModelSerializer):

    class Meta:
        model = Gcode
        exclude = ('id',)


class PlotSerializer(ModelSerializer):


    class Meta:
        model = Plot
        # fields = ('name', 'board', )
        exclude = ('id',)
