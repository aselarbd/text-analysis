from TermsAndConditions.serializer import Term, TermSerializer
from TermsAndConditions.models import TermDetails, TermHighLevel
from Handlers.Database.TermHandler import TermHandler
from PreProcessing import PreProcessing
from urllib.parse import urlparse
from Handlers.Cache.TermCache import TermCache


class TermService:
    """
    Term service handler class. Requests that comes to TermsAndConditionsAPI will handle by this service

    """

    dbHandler = TermHandler(details=TermDetails, highLevel=TermHighLevel)
    cacheHandler = TermCache

    @staticmethod
    def getAll():
        if len(TermService.cacheHandler.getAllTerm()) > 0:
            terms = TermService.cacheHandler.getAllTerm()
        else:
            terms = TermService.dbHandler.getAllTerm()
            TermService.cacheHandler.initializeTermCache(terms)
        serializer = TermSerializer(terms, many=True)
        return serializer.data

    @staticmethod
    def postTerm(request):
        termData = PreProcessing.getTerm(request.data['url'])
        termTitle = urlparse(request.data['url']).hostname.split(".")[1]
        termURL = request.data['url']
        term = Term(title=termTitle, url=termURL, data=termData)

        termID = TermService.dbHandler.addTerm(term)
        term.id = termID

        if len(TermService.cacheHandler.getAllTerm()) == 0:
            TermService.initializeCache()
        TermService.cacheHandler.addTerm(term)

        serializer = TermSerializer(term)
        return serializer.data

    @staticmethod
    def getTerm(ID):
        if len(TermService.cacheHandler.getAllTerm()) == 0:
            TermService.initializeCache()

        term = TermService.cacheHandler.getOneTerm(ID)
        if term:
            serializer = TermSerializer(term)
            return serializer.data
        else:
            term = TermService.dbHandler.getOneTerm(ID)
            if term:
                TermService.cacheHandler.addTerm(term)
                serializer = TermSerializer(term)
                return serializer.data
            else:
                return {"error message": "requested term not found in the database"}

    @staticmethod
    def deleteTerm(ID):
        if len(TermService.cacheHandler.getAllTerm()) == 0:
            TermService.initializeCache()

        term = TermService.dbHandler.deleteTerm(ID)
        if term:
            if TermService.cacheHandler.getOneTerm(ID):
                TermService.cacheHandler.deleteOneTerm(ID)
            serializer = TermSerializer(term)
            return serializer.data
        return {"error message": "requested term not found in the database"}

    @staticmethod
    def initializeCache():
        terms = TermService.dbHandler.getAllTerm()
        TermService.cacheHandler.initializeTermCache(terms)





