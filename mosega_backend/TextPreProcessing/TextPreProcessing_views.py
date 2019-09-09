from rest_framework import generics
from rest_framework import mixins

from TextPreProcessing.TextPreProcessing_Serializer import TextPreProcessingSerializer
from TextPreProcessing.models import TextPreProcessingModel


class TextPreProcessingList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TextPreProcessingModel.objects.all()
    serializer_class = TextPreProcessingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # TODO Intercept request.data and initiate the text pre processing
        return self.create(request, *args, **kwargs)


class TextPreProcessingDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                               generics.GenericAPIView):
    queryset = TextPreProcessingModel.objects.all()
    serializer_class = TextPreProcessingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
