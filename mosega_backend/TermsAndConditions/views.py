from rest_framework.views import APIView
from rest_framework.response import Response

from TermsAndConditions.service import get_all_terms, post_term, get_one_term, delete_one_term


class TermsAndConditionsList(APIView):

    def get(self, request):
        return Response(get_all_terms())

    def post(self, request):
        return Response(post_term(request))


class TermsAndConditionsDetails(APIView):

    def get(self, request, ID):
        return Response(get_one_term(ID))

    def delete(self, request, ID):
        return Response(delete_one_term(ID))
