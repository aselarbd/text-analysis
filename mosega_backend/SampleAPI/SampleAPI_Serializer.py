from rest_framework import serializers
from SampleAPI.models import SampleAPIModel


# SampleAPI serializer
class SampleAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleAPIModel
        fields = '__all__'
