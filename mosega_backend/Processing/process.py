from Processing.Utils import process_preparation
from Processing.Similar import Similar
from Processing.Cluster import Cluster
import Constants


def get_similar_clauses(query, clauses, item_id, database_ref, cache_ref):
    headings, descriptions, corpus = process_preparation(database=database_ref, cache=cache_ref, without_id=item_id)
    similar_set = Similar(query=query, clauses=clauses + 1, headings=headings, descriptions=descriptions,
                          corpus=corpus)

    if similar_set[0][Constants.SIMILARITY_ACCURACY] == 1.0 or similar_set[0][Constants.HEADING] == query:
        result_set = similar_set[1:]
    else:
        result_set = similar_set[:clauses]

    return result_set


def cluster_items(no_of_clusters, cache_ref, database_ref):
    headings, descriptions, corpus = process_preparation(cache=cache_ref, database=database_ref, without_id=None)
    return Cluster(no_of_clusters=no_of_clusters, headings=headings, descriptions=descriptions, corpus=corpus)
