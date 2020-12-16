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
        section_index = 1
        for data in term.data:
            if field == 'heading':
                TermCache.termProcessHeadingCache[str(term.id) + '_' + str(section_index)] = data[field]
            if field == 'text':
                TermCache.termProcessTextCache[str(term.id) + '_' + str(section_index)] = data[field]
            section_index += 1

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
    def get_all_headings_list():
        heading_list = []
        for key in TermCache.termProcessHeadingCache.keys():
            heading_list.append([key, TermCache.termProcessHeadingCache.get(key)])
        return heading_list

    @staticmethod
    def get_all_headings_except_one(item_id):
        heading_list = []
        for key in TermCache.termProcessHeadingCache.keys():
            if key.split("_")[0] != str(item_id):
                heading_list.append([key, TermCache.termProcessHeadingCache.get(key)])
        return heading_list

    @staticmethod
    def get_all_description_list():
        description_list = []
        for key in TermCache.termProcessTextCache.keys():
            description_list.append([key, TermCache.termProcessTextCache.get(key)])
        return description_list

    @staticmethod
    def get_all_descriptions_except_one(item_id):
        description_list = []
        for key in TermCache.termProcessTextCache.keys():
            if key.split("_")[0] != str(item_id):
                description_list.append([key, TermCache.termProcessTextCache.get(key)])
        return description_list

    @staticmethod
    def get_heading_and_description_list():
        headings = TermCache.get_all_headings_list()
        descriptions = TermCache.get_all_description_list()
        return headings, descriptions

    @staticmethod
    def get_headings_and_description_without_one(item_id):
        headings = TermCache.get_all_headings_except_one(item_id)
        descriptions = TermCache.get_all_descriptions_except_one(item_id)
        return headings, descriptions

    @staticmethod
    def getDescription(ID):
        return TermCache.termProcessTextCache.get(ID)

    @staticmethod
    def getHeadingList():
        value_list = list(TermCache.termProcessHeadingCache.values())
        key_list = list(TermCache.termProcessHeadingCache.keys())
        return key_list, value_list
