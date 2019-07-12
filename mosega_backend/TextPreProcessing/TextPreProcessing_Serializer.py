from rest_framework import serializers
from TextPreProcessing.models import TextPreProcessingModel


# TextPreProcessing serializer
class TextPreProcessingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPreProcessingModel
        fields = '__all__'
