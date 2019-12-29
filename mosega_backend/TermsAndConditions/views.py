from rest_framework.views import APIView
from rest_framework.response import Response

from TermsAndConditions.service import TermService


class TermsAndConditionsList(APIView):

    def get(self, request):
        return Response(TermService.getAll())

    def post(self, request):
        return Response(TermService.postTerm(request))


class TermsAndConditionsDetails(APIView):

    def get(self, request, ID):
        return Response(TermService.getTerm(ID))

    def delete(self, request, ID):
        return Response(TermService.deleteTerm(ID))
