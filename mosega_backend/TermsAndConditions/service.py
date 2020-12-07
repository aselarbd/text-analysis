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
        term_data = PreProcessing.getTerm(request.data['url'])
        term_title = urlparse(request.data['url']).hostname.split(".")[1]
        term_url = request.data['url']
        term = Term(title=term_title, url=term_url, data=term_data)

        term_id = TermService.dbHandler.addTerm(term)
        term.id = term_id

        if len(TermService.cacheHandler.getAllTerm()) == 0:
            TermService.initializeCache()
        TermService.cacheHandler.addTerm(term)

        serializer = TermSerializer(term)
        return serializer.data

    @staticmethod
    def getTerm(term_id):
        if len(TermService.cacheHandler.getAllTerm()) == 0:
            TermService.initializeCache()

        term = TermService.cacheHandler.getOneTerm(term_id)
        if term:
            serializer = TermSerializer(term)
            return serializer.data
        else:
            term = TermService.dbHandler.getOneTerm(term_id)
            if term:
                TermService.cacheHandler.addTerm(term)
                serializer = TermSerializer(term)
                return serializer.data
            else:
                return {"error message": "requested term not found in the database"}

    @staticmethod
    def deleteTerm(term_id):
        if len(TermService.cacheHandler.getAllTerm()) == 0:
            TermService.initializeCache()

        term = TermService.dbHandler.deleteTerm(term_id)
        if term:
            if TermService.cacheHandler.getOneTerm(term_id):
                TermService.cacheHandler.deleteOneTerm(term_id)
            serializer = TermSerializer(term)
            return serializer.data
        return {"error message": "requested term not found in the database"}

    @staticmethod
    def initializeCache():
        terms = TermService.dbHandler.getAllTerm()
        TermService.cacheHandler.initializeTermCache(terms)
