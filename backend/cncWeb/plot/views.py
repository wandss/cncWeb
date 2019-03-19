from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from .serializers import GcodeSerializer
from .models import Gcode


class GcodeListAPIView(ListAPIView):
    serializer_class = GcodeSerializer
    queryset = Gcode.objects.all()


class GcodeCreateAPIView(APIView):
    parser_classes = (FileUploadParser,)
    serializer_class = GcodeSerializer
    queryset = Gcode.objects.all()

    def post(self, request, filename, format=None):
        import pdb; pdb.set_trace()  #DEBUG
        document = request.data['file']
        gcode_file = Gcode.objets.create(gocode_file=document)
        gcode_file.save()
        data = {'filename': filename, 'id': gcode_file.id}
        return Response(data=data, status=status.HTTP_201_CREATED)
