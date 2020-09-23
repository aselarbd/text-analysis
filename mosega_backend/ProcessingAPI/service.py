from Processing.process import getSimilarClauses, doCluster
from Handlers.Database.PolicyHandler import PolicyHandler
from PrivacyPolicy.models import PolicyDetails, PolicyHighLevel
from Handlers.Database.TermHandler import TermHandler
from TermsAndConditions.models import TermDetails, TermHighLevel
from Handlers.Cache.PolicyCache import PolicyCache
from Handlers.Cache.TermCache import TermCache


class ProcessService:
    policyDBHandler = PolicyHandler(details=PolicyDetails, highLevel=PolicyHighLevel)
    termDBHandler = TermHandler(details=TermDetails, highLevel=TermHighLevel)
    policyCache = PolicyCache
    termCache = TermCache

    def __init__(self):
        self.initializeCache()

    # processing handling functions

    def handle(self, request):
        processType = request.data['processType']
        if processType == 'similar':
            return self.similarity(request)
        if processType == 'cluster':
            return self.getCluster(request)
        if processType == 'preCluster':
            return self.preCluster(request)

    def similarity(self, request):
        clauses = request.data['clauses']
        query = request.data['query']
        dataType = request.data['dataType']
        return getSimilarClauses(query=query, clauses=clauses, cacheType=dataType)

    def getCluster(self, request):
        dataType = request.data['dataType']
        noOfClusters = request.data['noOfClusters']
        return doCluster(noOfClusters=noOfClusters, cacheType=dataType)

    def preCluster(self, request):
        dataType = request.data['dataType']
        noOfClusters = request.data['noOfClusters']
        headerTitle = request.data['headerTitle']
        clusters = doCluster(noOfClusters=noOfClusters, cacheType=dataType)
        clusterNo = self.findClusterNumber(clusters, headerTitle)
        return clusters[clusterNo]

    # cache initialization

    def initializeCache(self):
        if len(self.termCache.getAllTerm()) == 0:
            self.initializeTermCache()
        if len(self.policyCache.getAllPolicy()) == 0:
            self.initializePolicyCache()

    def initializePolicyCache(self):
        policies = self.policyDBHandler.getAllPolicy()
        self.policyCache.initializePolicyCache(policies)

    def initializeTermCache(self):
        terms = self.termDBHandler.getAllTerm()
        self.termCache.initializeTermCache(terms)

    def findClusterNumber(self, clusters, headerTitle):
        for i in range(len(clusters)):
            for item in clusters[i]:
                if item['heading'] == headerTitle:
                    return i

