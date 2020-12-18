from Processing.Utils import process_preparation, exclude_same_topic_from_result
from Processing.Similar import Similar
from Processing.Cluster import Cluster


def get_similar_clauses(query, clauses, item_id, database_ref, cache_ref, include_all):
    headings, descriptions, corpus = process_preparation(database=database_ref, cache=cache_ref, without_id=item_id)
    similar_set = Similar(query=query, clauses=clauses + 1, headings=headings, descriptions=descriptions,
                          corpus=corpus)
    if include_all:
        # TODO : implement this
        pass

    result_set = exclude_same_topic_from_result(similar_set=similar_set, query=query, clauses=clauses)

    return result_set


def cluster_items(no_of_clusters, cache_ref, database_ref):
    headings, descriptions, corpus = process_preparation(cache=cache_ref, database=database_ref, without_id=None)
    return Cluster(no_of_clusters=no_of_clusters, headings=headings, descriptions=descriptions, corpus=corpus)
