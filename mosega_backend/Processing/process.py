from sentence_transformers import SentenceTransformer
from Handlers.Database.PolicyHandler import PolicyHandler
from Handlers.Database.TermHandler import TermHandler
from TermsAndConditions.models import TermHighLevel, TermDetails
from PrivacyPolicy.models import PolicyDetails, PolicyHighLevel
import scipy.spatial
from sklearn.cluster import AgglomerativeClustering
from Handlers.Cache.PolicyCache import PolicyCache
from Handlers.Cache.TermCache import TermCache


def getSimilarClauses(query, clauses, cacheType):
    headings, descriptions, corpus_embeddings = processPreparation(cacheType)
    resultList = []

    queries = [query]
    query_embeddings = embedder.encode(queries)

    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        for ID, distance in results[0:clauses]:
            resultList.append({"heading": headings[ID][1].strip(),
                               "text": descriptions[ID][1].strip(),
                               "accuracy": 1 - distance})
    return resultList


# noinspection PyTypeChecker
def doCluster(noOfClusters, cacheType):
    headings, descriptions, corpus_embeddings = processPreparation(cacheType)
    clusters = [[] for i in range(noOfClusters)]

    clusteringModel = AgglomerativeClustering(n_clusters=noOfClusters)
    clusteringModel.fit(corpus_embeddings)
    clusterAssignment = clusteringModel.labels_

    for ID, clusterId in enumerate(clusterAssignment):
        clusters[clusterId].append({"heading": headings[ID][1].strip(),
                                    "text": descriptions[ID][1].strip()})
    return clusters


def processPreparation(cacheType):
    if cacheType == 'policy':
        cache = PolicyCache
        db = policyDBHandler
        prev_corpus = policy_embeddings
    else:
        cache = TermCache
        db = termDBHandler
        prev_corpus = term_embeddings

    headings, descriptions = getHeadingsAndDescriptionList(db=db, cache=cache)
    updateCorpus = corpusChecker(cache, prev_corpus, headings)

    if updateCorpus is not None:
        corpus_embeddings = [*prev_corpus, *updateCorpus]
    else:
        corpus_embeddings = prev_corpus

    return headings, descriptions, corpus_embeddings


def getColumn(matrix, i):
    return [row[i] for row in matrix]


def corpusChecker(cache, corpus_embeddings, headings):
    currentHeadingsList = cache.getAllHeadingsList()
    if len(corpus_embeddings) < len(currentHeadingsList):
        newHeadings = getColumn(matrix=currentHeadingsList[len(corpus_embeddings):len(currentHeadingsList)], i=1)
        return embedder.encode(newHeadings)
    return None


def getHeadingsAndDescriptionList(db, cache):
    headings, descriptions = cache.getHeadingAndDescriptionList()

    if len(headings) == 0 or len(descriptions) == 0:
        headings, descriptions = db.getAllHeadingAndDescriptionList()
    return headings, descriptions


embedder = SentenceTransformer('bert-base-nli-mean-tokens')

# Data loading via DB
policyDBHandler = PolicyHandler(details=PolicyDetails, highLevel=PolicyHighLevel)
termDBHandler = TermHandler(details=TermDetails, highLevel=TermHighLevel)

policyCorpusHeadings, policyCorpusDescription = policyDBHandler.getAllHeadingAndDescriptionList()
policyCorpus = getColumn(matrix=policyCorpusHeadings, i=1)

termCorpusHeadings, termCorpusDescription = termDBHandler.getAllHeadingAndDescriptionList()
termCorpus = getColumn(matrix=termCorpusHeadings, i=1)

# embed corpus with bert
policy_embeddings = embedder.encode(policyCorpus)
term_embeddings = embedder.encode(termCorpus)
