from django.shortcuts import render

from SampleAPI.models import SampleAPIModel
from SampleAPI.SampleAPI_Serializer import SampleAPISerializer
from rest_framework import mixins
from rest_framework import generics


class SampleAPIList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = SampleAPIModel.objects.all()
    serializer_class = SampleAPISerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SampleAPIDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    queryset = SampleAPIModel.objects.all()
    serializer_class = SampleAPISerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
