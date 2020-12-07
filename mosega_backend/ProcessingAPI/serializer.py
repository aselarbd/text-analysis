from rest_framework import serializers


# Processing serializer
from ProcessingAPI.models import ProcessingAPIModel


class ProcessingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingAPIModel
