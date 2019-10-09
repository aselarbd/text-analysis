from rest_framework import serializers
from TermsAndConditions.models import TermsAndConditionsModel


# TermsAndConditions serializer
class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndConditionsModel
        fields = ['Term', 'created_at', 'id', 'term_url', 'term_heading']
