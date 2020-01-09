def getColumn(matrix, i):
    return [row[i] for row in matrix]


def getHeadingsAndDescriptionList(db, cache):
    headings, descriptions = cache.getHeadingAndDescriptionList()

    if len(headings) == 0 or len(descriptions) == 0:
        headings, descriptions = db.getAllHeadingAndDescriptionList()
    return headings, descriptions


def corpusChecker(cache, corpus, embedder):
    currentHeadingsList = cache.getAllHeadingsList()
    if len(corpus) < len(currentHeadingsList):
        newHeadings = getColumn(matrix=currentHeadingsList[len(corpus):len(currentHeadingsList)], i=1)
        return embedder.encode(newHeadings)
    return None


