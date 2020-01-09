from rest_framework.views import APIView
from rest_framework.response import Response
from ProcessingAPI.service import ProcessService


class Processing(APIView):

    processingService = ProcessService()

    def post(self, request):
        return Response(self.processingService.handle(request))
