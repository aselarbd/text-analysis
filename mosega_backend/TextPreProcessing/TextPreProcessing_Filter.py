from TextPreProcessing.models import TextPreProcessingModel
from TextPreProcessing.TextPreProcessing_Serializer import TextPreProcessingSerializer
from rest_framework import generics


class TextAPIRequestFilter(generics.ListAPIView):
    serializer_class = TextPreProcessingSerializer


