from SampleAPI.models import SampleAPIModel
from SampleAPI.SampleAPI_Serializer import SampleAPISerializer
from rest_framework import viewsets, permissions


# SampleAPI viewset

class SampleAPIViewSet(viewsets.ModelViewSet):

    queryset = SampleAPIModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SampleAPISerializer

