class TermCache:
    """
    Term of conditions cache handler

    """

    termObjectCache = {}
    termProcessHeadingCache = {}
    termProcessTextCache = {}

    # Term CRUD caching functions

    @staticmethod
    def initializeTermCache(terms):
        TermCache.initializeTermObjectCache(terms)
        TermCache.initializeTermProcessHeadingCache(terms)
        TermCache.initializeTermProcessTextCache(terms)

    @staticmethod
    def initializeTermObjectCache(terms):
        for term in terms:
            TermCache.addTerm(term)

    @staticmethod
    def initializeTermProcessHeadingCache(terms):
        for term in terms:
            TermCache.addProcessDecAndTextCache(term, 'heading')

    @staticmethod
    def initializeTermProcessTextCache(terms):
        for term in terms:
            TermCache.addProcessDecAndTextCache(term, 'text')

    @staticmethod
    def addTerm(term):
        TermCache.termObjectCache[str(term.id)] = term
        TermCache.addProcessDecAndTextCache(term, 'heading')
        TermCache.addProcessDecAndTextCache(term, 'text')

    @staticmethod
    def addProcessDecAndTextCache(term, field):
        sectionIndex = 1
        for data in term.data:
            if field == 'heading':
                TermCache.termProcessHeadingCache[str(term.id) + '_' + str(sectionIndex)] = data[field]
            if field == 'text':
                TermCache.termProcessTextCache[str(term.id) + '_' + str(sectionIndex)] = data[field]
            sectionIndex += 1

    @staticmethod
    def getAllTerm():
        return TermCache.termObjectCache.values()

    @staticmethod
    def getOneTerm(ID):
        ID = str(ID)
        return TermCache.termObjectCache.get(ID)

    @staticmethod
    def deleteOneTerm(ID):
        ID = str(ID)
        if TermCache.termObjectCache.get(ID):
            term = TermCache.termObjectCache.get(ID)
            del TermCache.termObjectCache[ID]
            TermCache.deleteTermDesAndText(ID, 'heading')
            TermCache.deleteTermDesAndText(ID, 'text')

            return term
        else:
            return None

    @staticmethod
    def deleteTermDesAndText(ID, field):
        if field == 'heading':
            for k in list(TermCache.termProcessHeadingCache.keys()):
                if k.startswith(ID):
                    del TermCache.termProcessHeadingCache[k]
        if field == 'text':
            for k in list(TermCache.termProcessTextCache.keys()):
                if k.startswith(ID):
                    del TermCache.termProcessTextCache[k]

    # ProcessingAPI caching functions

    @staticmethod
    def getAllHeadingsList():
        headingList = []
        for key in TermCache.termProcessHeadingCache.keys():
            headingList.append([key, TermCache.termProcessHeadingCache.get(key)])
        return headingList

    @staticmethod
    def getAllDescriptionList():
        descriptionList = []
        for key in TermCache.termProcessTextCache.keys():
            descriptionList.append([key, TermCache.termProcessTextCache.get(key)])
        return descriptionList

    @staticmethod
    def getHeadingAndDescriptionList():
        headings = TermCache.getAllHeadingsList()
        descriptions = TermCache.getAllDescriptionList()
        return headings, descriptions

    @staticmethod
    def getDescription(ID):
        return TermCache.termProcessTextCache.get(ID)

    @staticmethod
    def getHeadingList():
        valueList = list(TermCache.termProcessHeadingCache.values())
        keyList = list(TermCache.termProcessHeadingCache.keys())
        return keyList, valueList
