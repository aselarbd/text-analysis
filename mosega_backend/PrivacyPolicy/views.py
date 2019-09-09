from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from PrivacyPolicy.serializer import PrivacyPolicySerializer
from PrivacyPolicy.models import PrivacyPolicyModel

from PreProcessing import PreProcessing


class PrivacyPolicyList(APIView):

    def get(self, request):
        policy = PrivacyPolicyModel.objects.all()
        serializer = PrivacyPolicySerializer(policy, many=True)
        return Response(serializer.data)

    def post(self, request):
        # TODO Intercept request.data and initiate the text pre processing
        pre_processed_policy = PreProcessing.preprocess_pipeline(request.data['url'])

        serializer = PrivacyPolicySerializer(data={"PrivacyPolicy": pre_processed_policy})

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
