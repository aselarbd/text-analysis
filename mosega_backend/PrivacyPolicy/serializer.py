from rest_framework import serializers
from PrivacyPolicy.models import PrivacyPolicyModel


# PrivacyPolicy serializer
class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicyModel
        fields = ['PrivacyPolicy', 'created_at', 'id', 'policy_url', 'policy_heading', 'type']
