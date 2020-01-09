class PolicyCache:
    """
    Privacy policy cache handler

    """

    policyObjectCache = {}
    policyProcessHeadingCache = {}
    policyProcessTextCache = {}

    # Policy CRUD caching functions

    @staticmethod
    def initializePolicyCache(policies):
        PolicyCache.initializePolicyObjectCache(policies)
        PolicyCache.initializePolicyProcessHeadingCache(policies)
        PolicyCache.initializePolicyProcessTextCache(policies)

    @staticmethod
    def initializePolicyObjectCache(policies):
        for policy in policies:
            PolicyCache.addPolicy(policy)

    @staticmethod
    def initializePolicyProcessHeadingCache(policies):
        for policy in policies:
            PolicyCache.addProcessDecAndTextCache(policy, 'heading')

    @staticmethod
    def initializePolicyProcessTextCache(policies):
        for policy in policies:
            PolicyCache.addProcessDecAndTextCache(policy, 'text')

    @staticmethod
    def addPolicy(policy):
        PolicyCache.policyObjectCache[str(policy.id)] = policy
        PolicyCache.addProcessDecAndTextCache(policy, 'heading')
        PolicyCache.addProcessDecAndTextCache(policy, 'text')

    @staticmethod
    def addProcessDecAndTextCache(policy, field):
        sectionIndex = 1
        for data in policy.data:
            if field == 'heading':
                PolicyCache.policyProcessHeadingCache[str(policy.id) + '_' + str(sectionIndex)] = data[field]
            if field == 'text':
                PolicyCache.policyProcessTextCache[str(policy.id) + '_' + str(sectionIndex)] = data[field]
            sectionIndex += 1

    @staticmethod
    def getAllPolicy():
        return PolicyCache.policyObjectCache.values()

    @staticmethod
    def getOnePolicy(ID):
        ID = str(ID)
        return PolicyCache.policyObjectCache.get(ID)

    @staticmethod
    def deleteOnePolicy(ID):
        ID = str(ID)
        if PolicyCache.policyObjectCache.get(ID):
            policy = PolicyCache.policyObjectCache.get(ID)
            del PolicyCache.policyObjectCache[ID]
            PolicyCache.deletePolicyDesAndText(ID, 'heading')
            PolicyCache.deletePolicyDesAndText(ID, 'text')

            return policy
        else:
            return None

    @staticmethod
    def deletePolicyDesAndText(ID, field):
        if field == 'heading':
            for k in list(PolicyCache.policyProcessHeadingCache.keys()):
                if k.startswith(ID):
                    del PolicyCache.policyProcessHeadingCache[k]
        if field == 'text':
            for k in list(PolicyCache.policyProcessTextCache.keys()):
                if k.startswith(ID):
                    del PolicyCache.policyProcessTextCache[k]

    # ProcessingAPI caching functions

    @staticmethod
    def getAllHeadingsList():
        headingList = []
        for key in PolicyCache.policyProcessHeadingCache.keys():
            headingList.append([key, PolicyCache.policyProcessHeadingCache.get(key)])
        return headingList

    @staticmethod
    def getAllDescriptionList():
        descriptionList = []
        for key in PolicyCache.policyProcessTextCache.keys():
            descriptionList.append([key, PolicyCache.policyProcessTextCache.get(key)])
        return descriptionList

    @staticmethod
    def getHeadingAndDescriptionList():
        headings = PolicyCache.getAllHeadingsList()
        descriptions = PolicyCache.getAllDescriptionList()
        return headings, descriptions

    @staticmethod
    def getDescription(ID):
        return PolicyCache.policyProcessTextCache.get(ID)

    @staticmethod
    def getHeadingList():
        valueList = list(PolicyCache.policyProcessHeadingCache.values())
        keyList = list(PolicyCache.policyProcessHeadingCache.keys())
        return keyList, valueList
