from PrivacyPolicy.models import PolicyDetails, PolicyHighLevel
from PrivacyPolicy.serializer import Policy


class PolicyHandler:

    def __init__(self, highLevel, details):
        self.highLevel = highLevel
        self.details = details

    def getAllPolicy(self):
        policyList = []
        policyHL = self.highLevel.objects.order_by('PolicyID')

        for i in range(len(policyHL)):
            details = self.detailsHelper(self.details.objects.filter(PolicyID=policyHL[i].PolicyID))
            policy = Policy(title=policyHL[i].PolicyTitle, url=policyHL[i].PolicyURL, data=details)
            policy.id = policyHL[i].PolicyID
            policyList.append(policy)

        return policyList

    def getOnePolicy(self, ID):
        policyHL = self.highLevel.objects.filter(PolicyID=ID)
        if len(policyHL) > 0:
            policyDetails = self.detailsHelper(self.details.objects.filter(PolicyID=ID))
            policy = Policy(title=policyHL[0].PolicyTitle, url=policyHL[0].PolicyURL, data=policyDetails)
            policy.id = ID
            return policy
        return None

    def detailsHelper(self, details):
        detailsList = []
        for obj in details:
            detailsList.append({"heading": obj.heading, "text": obj.text})
        return detailsList

    def addPolicy(self, policy):
        policyID = len(self.highLevel.objects.order_by('PolicyID')) + 1

        # Save data in PolicyHighLevel table
        policyHighLevel = PolicyHighLevel(PolicyID=policyID, PolicyURL=policy.url, PolicyTitle=policy.title)
        policyHighLevel.save()

        # Save data in PolicyDetails table
        for i in range(len(policy.data)):
            data = policy.data[i]
            policyDetails = PolicyDetails(PolicyID=policyID, SectionID=i + 1, heading=data['heading'],
                                          text=data['text'])
            policyDetails.save()
        return policyID

    def deletePolicy(self, ID):
        policy = self.getOnePolicy(ID)
        if policy:
            self.highLevel.objects.get(PolicyID=ID).delete()
            self.details.objects.filter(PolicyID=ID).delete()
            return policy
        return None
