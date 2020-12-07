from sentence_transformers import SentenceTransformer
from Handlers.Cache.PolicyCache import PolicyCache
from Handlers.Cache.TermCache import TermCache
from Handlers.Database.PolicyHandler import PolicyHandler
from Handlers.Database.TermHandler import TermHandler
from TermsAndConditions.models import TermHighLevel, TermDetails
from PrivacyPolicy.models import PolicyDetails, PolicyHighLevel
from Processing.Utils import getColumn, getHeadingsAndDescriptionList, corpusChecker
from Processing.Similar import Similar
from Processing.Cluster import Cluster

embedder = SentenceTransformer('bert-base-nli-mean-tokens')

# Data loading via DB
policyDBHandler = PolicyHandler(details=PolicyDetails, highLevel=PolicyHighLevel)
termDBHandler = TermHandler(details=TermDetails, highLevel=TermHighLevel)

policyCorpusHeadings, policyCorpusDescription = policyDBHandler.getAllHeadingAndDescriptionList()
policyCorpus = getColumn(matrix=policyCorpusHeadings, i=1)

termCorpusHeadings, termCorpusDescription = termDBHandler.getAllHeadingAndDescriptionList()
termCorpus = getColumn(matrix=termCorpusHeadings, i=1)

# embed corpus with bert
policyEmbeddings = embedder.encode(policyCorpus)
termEmbeddings = embedder.encode(termCorpus)


def corpusUpdate(newCorpus, cacheType):
    if cacheType == "policy":
        global policyEmbeddings
        policyEmbeddings = newCorpus
    elif cacheType == "term":
        global termEmbeddings
        termEmbeddings = newCorpus


def processPreparation(cacheType, languageModel):
    if cacheType == 'policy':
        cache = PolicyCache
        db = policyDBHandler
        previousCorpus = policyEmbeddings
    else:
        cache = TermCache
        db = termDBHandler
        previousCorpus = termEmbeddings

    headings, descriptions = getHeadingsAndDescriptionList(db=db, cache=cache)
    updatedCorpus = corpusChecker(cache=cache, corpus=previousCorpus, embedder=languageModel)

    if updatedCorpus is not None:
        newCorpus = [*previousCorpus, *updatedCorpus]
    else:
        newCorpus = previousCorpus

    return headings, descriptions, newCorpus


# Processing functions

def getSimilarClauses(query, clauses, cacheType):
    headings, descriptions, corpus = processPreparation(cacheType=cacheType, languageModel=embedder)
    corpusUpdate(newCorpus=corpus, cacheType=cacheType)
    return Similar(query=query, clauses=clauses, headings=headings, descriptions=descriptions, corpus=corpus,
                   embedder=embedder)


def doCluster(noOfClusters, cacheType):
    headings, descriptions, corpus = processPreparation(cacheType=cacheType, languageModel=embedder)
    corpusUpdate(newCorpus=corpus, cacheType=cacheType)
    return Cluster(noOfClusters=noOfClusters, headings=headings, descriptions=descriptions, corpus=corpus)
