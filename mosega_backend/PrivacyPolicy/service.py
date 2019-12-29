from PrivacyPolicy.serializer import Policy, PolicySerializer
from PrivacyPolicy.models import PolicyDetails, PolicyHighLevel
from Handlers.Database.PolicyHandler import PolicyHandler
from PreProcessing import PreProcessing
from urllib.parse import urlparse


class PolicyService:
    """
    Policy service handler class. Requests that comes to PrivacyPolicyAPI will handle by this service

    """

    dbHandler = PolicyHandler(details=PolicyDetails, highLevel=PolicyHighLevel)

    @staticmethod
    def getAll():
        policies = PolicyService.dbHandler.getAllPolicy()
        serializer = PolicySerializer(policies, many=True)
        return serializer.data

    @staticmethod
    def postPolicy(request):
        policyData = PreProcessing.getPolicy(request.data['url'])
        policyTitle = urlparse(request.data['url']).hostname.split(".")[1]
        policyURL = request.data['url']
        policy = Policy(title=policyTitle, url=policyURL, data=policyData)

        policyID = PolicyService.dbHandler.addPolicy(policy)
        serializer = PolicySerializer(policy)
        serializer.data['id'] = policyID
        policyRes = serializer.data
        policyRes['id'] = policyID
        return policyRes

    @staticmethod
    def getPolicy(ID):
        policy = PolicyService.dbHandler.getOnePolicy(ID)
        if policy:
            serializer = PolicySerializer(policy)
            return serializer.data
        return {"error message": "requested policy not found in the database"}

    @staticmethod
    def deletePolicy(ID):
        policy = PolicyService.dbHandler.deletePolicy(ID)
        if policy:
            serializer = PolicySerializer(policy)
            return serializer.data
        return {"error message": "requested policy not found in the database"}





