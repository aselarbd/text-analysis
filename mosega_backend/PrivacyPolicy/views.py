from rest_framework.views import APIView
from rest_framework.response import Response

from PrivacyPolicy.service import PolicyService


class PrivacyPolicyList(APIView):

    def get(self, request):
        return Response(PolicyService.getAll())

    def post(self, request):
        return Response(PolicyService.postPolicy(request))


class PrivacyPolicyDetails(APIView):

    def get(self, request, ID):
        return Response(PolicyService.getPolicy(ID))

    def delete(self, request, ID):
        return Response(PolicyService.deletePolicy(ID))
