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
        policy_data = PreProcessing.getPolicy(request.data['url'])
        policy_title = urlparse(request.data['url']).hostname.split(".")[1]
        policy_url = request.data['url']
        policy = Policy(title=policy_title, url=policy_url, data=policy_data)

        policy_id = PolicyService.dbHandler.addPolicy(policy)
        policy.id = policy_id

        if len(PolicyService.cacheHandler.getAllPolicy()) == 0:
            PolicyService.initializeCache()
        PolicyService.cacheHandler.addPolicy(policy)

        serializer = PolicySerializer(policy)
        return serializer.data

    @staticmethod
    def getPolicy(policy_id):

        if len(PolicyService.cacheHandler.getAllPolicy()) == 0:
            PolicyService.initializeCache()

        policy = PolicyService.cacheHandler.getOnePolicy(policy_id)

        if policy:
            serializer = PolicySerializer(policy)
            return serializer.data
        else:
            policy = PolicyService.dbHandler.getOnePolicy(policy_id)
            if policy:
                PolicyService.cacheHandler.addPolicy(policy)
                serializer = PolicySerializer(policy)
                return serializer.data
            else:
                return {"error message": "requested policy not found in the database"}

    @staticmethod
    def deletePolicy(policy_id):

        if len(PolicyService.cacheHandler.getAllPolicy()) == 0:
            PolicyService.initializeCache()

        policy = PolicyService.dbHandler.deletePolicy(policy_id)
        if policy:
            if PolicyService.cacheHandler.getOnePolicy(policy_id):
                PolicyService.cacheHandler.deleteOnePolicy(policy_id)
            serializer = PolicySerializer(policy)
            return serializer.data
        return {"error message": "requested policy not found in the database"}

    @staticmethod
    def initializeCache():
        policies = PolicyService.dbHandler.getAllPolicy()
        PolicyService.cacheHandler.initializePolicyCache(policies)
