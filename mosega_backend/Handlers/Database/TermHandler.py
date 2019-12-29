from Handlers.Database.Utils import detailsHelper
from TermsAndConditions.models import TermHighLevel, TermDetails
from TermsAndConditions.serializer import Term


class TermHandler:

    def __init__(self, highLevel, details):
        self.highLevel = highLevel
        self.details = details

    def getAllTerm(self):
        termList = []
        termHL = self.highLevel.objects.order_by('TermID')

        for i in range(len(termHL)):
            details = detailsHelper(self.details.objects.filter(TermID=termHL[i].TermID))
            term = Term(title=termHL[i].TermTitle, url=termHL[i].TermURL, data=details)
            term.id = termHL[i].TermID
            termList.append(term)

        return termList

    def getOneTerm(self, ID):
        termHL = self.highLevel.objects.filter(TermID=ID)
        if len(termHL) > 0:
            termDetails = detailsHelper(self.details.objects.filter(TermID=ID))
            term = Term(title=termHL[0].TermTitle, url=termHL[0].TermURL, data=termDetails)
            term.id = ID
            return term
        return None

    def addTerm(self, term):
        termID = len(self.highLevel.objects.order_by('TermID')) + 1

        # Save data in TermHighLevel table
        termHighLevel = TermHighLevel(TermID=termID, TermURL=term.url, TermTitle=term.title)
        termHighLevel.save()

        # Save data in TermDetails table
        for i in range(len(term.data)):
            data = term.data[i]
            termDetails = TermDetails(TermID=termID, SectionID=i + 1, heading=data['heading'],
                                      text=data['text'])
            termDetails.save()
        return termID

    def deleteTerm(self, ID):
        term = self.getOneTerm(ID)
        if term:
            self.highLevel.objects.filter(TermID=ID).delete()
            self.details.objects.filter(TermID=ID).delete()
            return term
        return None
