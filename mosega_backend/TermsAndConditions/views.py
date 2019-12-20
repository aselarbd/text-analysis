from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from urllib.parse import urlparse

from TermsAndConditions.serializer import TermsAndConditionsSerializer
from TermsAndConditions.models import TermsAndConditionsModel

from PreProcessing import PreProcessing


class TermsAndConditionsList(APIView):

    def get(self, request):
        term = TermsAndConditionsModel.objects.all()
        serializer = TermsAndConditionsSerializer(term, many=True)
        return Response(serializer.data)

    def post(self, request):
        pre_processed_term = PreProcessing.getTerm(request.data['url'])

        term = {"Term": pre_processed_term, "term_url": request.data['url'],
                "term_heading": urlparse(request.data['url']).hostname.split(".")[1]}

        serializer = TermsAndConditionsSerializer(data=term)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TermsAndConditionsDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                generics.GenericAPIView):
    queryset = TermsAndConditionsModel.objects.all()
    serializer_class = TermsAndConditionsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
