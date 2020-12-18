from rest_framework.views import APIView
from rest_framework.response import Response

from PrivacyPolicy.service import get_all_policies, post_policy, get_one_policy, delete_one_policy


class PrivacyPolicyList(APIView):

    def get(self, request):
        return Response(get_all_policies())

    def post(self, request):
        return Response(post_policy(request))


class PrivacyPolicyDetails(APIView):

    def get(self, request, ID):
        return Response(get_one_policy(ID))

    def delete(self, request, ID):
        return Response(delete_one_policy(ID))
