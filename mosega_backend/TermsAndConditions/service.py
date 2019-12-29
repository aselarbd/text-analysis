from TermsAndConditions.serializer import Term, TermSerializer
from TermsAndConditions.models import TermDetails, TermHighLevel
from Handlers.Database.TermHandler import TermHandler
from PreProcessing import PreProcessing
from urllib.parse import urlparse


class TermService:
    """
    Term service handler class. Requests that comes to TermsAndConditionsAPI will handle by this service

    """

    dbHandler = TermHandler(details=TermDetails, highLevel=TermHighLevel)

    @staticmethod
    def getAll():
        terms = TermService.dbHandler.getAllTerm()
        serializer = TermSerializer(terms, many=True)
        return serializer.data

    @staticmethod
    def postTerm(request):
        termData = PreProcessing.getTerm(request.data['url'])
        termTitle = urlparse(request.data['url']).hostname.split(".")[1]
        termURL = request.data['url']
        term = Term(title=termTitle, url=termURL, data=termData)

        termID = TermService.dbHandler.addTerm(term)
        serializer = TermSerializer(term)
        serializer.data['id'] = termID
        termRes = serializer.data
        termRes['id'] = termID
        return termRes

    @staticmethod
    def getTerm(ID):
        term = TermService.dbHandler.getOneTerm(ID)
        if term:
            serializer = TermSerializer(term)
            return serializer.data
        return {"error message": "requested term not found in the database"}

    @staticmethod
    def deleteTerm(ID):
        term = TermService.dbHandler.deleteTerm(ID)
        if term:
            serializer = TermSerializer(term)
            return serializer.data
        return {"error message": "requested term not found in the database"}





