from rest_framework.views import APIView
from rest_framework.response import Response

from TermsAndConditions.serializer import TermsAndConditionsSerializer
from TermsAndConditions.models import TermsAndConditionsModel


class ProcessingOne(APIView):

    def get(self, request):

        return Response({"test":"processing"})


