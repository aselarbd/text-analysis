import scipy.spatial
from sentence_transformers import SentenceTransformer
import Constants


def Similar(query, clauses, headings, descriptions, corpus):
    result_list = []

    queries = [query]
    embedder = SentenceTransformer(Constants.SENTENCE_TRANSFORMER)
    query_embeddings = embedder.encode(queries)

    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding], corpus, Constants.SIMILARITY_DISTANCE)[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        for ID, distance in results[0:clauses]:
            result_list.append({Constants.HEADING: headings[ID][1].strip(),
                               Constants.TEXT: descriptions[ID][1].strip(),
                               Constants.SIMILARITY_ACCURACY: 1 - distance})
    return result_list
