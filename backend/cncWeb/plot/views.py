from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from .serializers import GcodeSerializer, PlotSerializer
from .models import Gcode, Plot


class GcodeListAPIView(ListAPIView):
    serializer_class = GcodeSerializer
    queryset = Gcode.objects.all()


class GcodeCreateAPIView(APIView):
    parser_classes = (FileUploadParser,)
    serializer_class = GcodeSerializer
    queryset = Gcode.objects.all()

    def post(self, request, filename, format=None):
        document = request.data['file']
        gcode_file = Gcode.objects.create(gcode_file=document)
        gcode_file.save()
        data = {'filename': filename, 'id': gcode_file.id}
        return Response(data=data, status=status.HTTP_201_CREATED)

class PlotListCreateAPIView(ListCreateAPIView):

    serializer_class = PlotSerializer
    queryset = Plot.objects.all()
