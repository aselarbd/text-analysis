from PrivacyPolicy.serializer import Policy, PolicySerializer
from PrivacyPolicy.models import PolicyDetails, PolicyHighLevel
from Handlers.Database.PolicyHandler import PolicyHandler
from PreProcessing import PreProcessing
from urllib.parse import urlparse
from Handlers.Cache.PolicyCache import PolicyCache


class PolicyService:
    """
    Policy service handler class. Requests that comes to PrivacyPolicyAPI will handle by this service

    """

    dbHandler = PolicyHandler(details=PolicyDetails, highLevel=PolicyHighLevel)
    cacheHandler = PolicyCache

    @staticmethod
    def getAll():
        if len(PolicyService.cacheHandler.getAllPolicy()) > 0:
            policies = PolicyService.cacheHandler.getAllPolicy()
        else:
            policies = PolicyService.dbHandler.getAllPolicy()
            PolicyService.cacheHandler.initializePolicyCache(policies)
        serializer = PolicySerializer(policies, many=True)
        return serializer.data

    @staticmethod
    def postPolicy(request):
        policyData = PreProcessing.getPolicy(request.data['url'])
        policyTitle = urlparse(request.data['url']).hostname.split(".")[1]
        policyURL = request.data['url']
        policy = Policy(title=policyTitle, url=policyURL, data=policyData)

        policyID = PolicyService.dbHandler.addPolicy(policy)
        policy.id = policyID

        if len(PolicyService.cacheHandler.getAllPolicy()) == 0:
            PolicyService.initializeCache()
        PolicyService.cacheHandler.addPolicy(policy)

        serializer = PolicySerializer(policy)
        return serializer.data

    @staticmethod
    def getPolicy(ID):

        if len(PolicyService.cacheHandler.getAllPolicy()) == 0:
            PolicyService.initializeCache()

        policy = PolicyService.cacheHandler.getOnePolicy(ID)

        if policy:
            serializer = PolicySerializer(policy)
            return serializer.data
        else:
            policy = PolicyService.dbHandler.getOnePolicy(ID)
            if policy:
                PolicyService.cacheHandler.addPolicy(policy)
                serializer = PolicySerializer(policy)
                return serializer.data
            else:
                return {"error message": "requested policy not found in the database"}

    @staticmethod
    def deletePolicy(ID):

        if len(PolicyService.cacheHandler.getAllPolicy()) == 0:
            PolicyService.initializeCache()

        policy = PolicyService.dbHandler.deletePolicy(ID)
        if policy:
            if PolicyService.cacheHandler.getOnePolicy(ID):
                PolicyService.cacheHandler.deleteOnePolicy(ID)
            serializer = PolicySerializer(policy)
            return serializer.data
        return {"error message": "requested policy not found in the database"}

    @staticmethod
    def initializeCache():
        policies = PolicyService.dbHandler.getAllPolicy()
        PolicyService.cacheHandler.initializePolicyCache(policies)
