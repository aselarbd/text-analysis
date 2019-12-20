from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from urllib.parse import urlparse

from PrivacyPolicy.serializer import PrivacyPolicySerializer
from PrivacyPolicy.models import PrivacyPolicyModel

from PreProcessing import PreProcessing


class PrivacyPolicyList(APIView):

    def get(self, request):
        policy = PrivacyPolicyModel.objects.all()
        serializer = PrivacyPolicySerializer(policy, many=True)
        return Response(serializer.data)

    def post(self, request):
        pre_processed_policy = PreProcessing.getPolicy(request.data['url'])

        policy = {
            "PrivacyPolicy": pre_processed_policy,
            "type": "privacyPolicy",
            "policy_url": request.data['url'],
            "policy_heading": urlparse(request.data['url']).hostname.split(".")[1]
        }

        serializer = PrivacyPolicySerializer(data=policy)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrivacyPolicyDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = PrivacyPolicyModel.objects.all()
    serializer_class = PrivacyPolicySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
