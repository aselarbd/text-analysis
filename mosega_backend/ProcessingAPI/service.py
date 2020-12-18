from Processing.Utils import cache_update, find_cluster_number, get_cache_and_db
from Processing.process import get_similar_clauses, cluster_items
from Processing.TextPreProcess import textPreProcess
from Database.Main import get_database_reference
from Cache.Main import get_cache_reference
import Constants


class ProcessService:

    def __init__(self):
        self.term_database = get_database_reference(Constants.TERM)
        self.term_cache = get_cache_reference(Constants.TERM)

        self.policy_database = get_database_reference(Constants.POLICY)
        self.policy_cache = get_cache_reference(Constants.POLICY)

        cache_update(cache_ref=self.term_cache, database_ref=self.term_database)
        cache_update(cache_ref=self.policy_cache, database_ref=self.policy_database)

    def handle(self, request):
        process_type = request.data[Constants.PROCESS_IDENTIFIER]
        if process_type == Constants.PROCESS_SIMILARITY:
            return self.similarity(request)
        if process_type == Constants.PROCESS_CLUSTER:
            return self.create_clusters(request)
        if process_type == Constants.PROCESS_PRE_CLUSTER:
            return self.create_pre_cluster(request)
        if process_type == Constants.PROCESS_SIMILARITY_FROM_TOPIC:
            return self.similarity_set(request)
        if process_type == Constants.PROCESS_SIMILARITY_FROM_TEXT:
            request.data[Constants.QUERY] = textPreProcess(request.data[Constants.QUERY])
            return self.similarity(request)

    def similarity(self, request):
        clauses = request.data[Constants.CLAUSES]
        query = request.data[Constants.QUERY]
        data_type = request.data[Constants.DATA_TYPE]
        item_id = request.data[Constants.ITEM_ID]

        db, cache = self.select_db_cache(data_type=data_type)
        return get_similar_clauses(query=query, clauses=clauses, item_id=item_id, database_ref=db,
                                   cache_ref=cache)

    def similarity_set(self, request):
        data_type = request.data[Constants.DATA_TYPE]
        item_id = request.data[Constants.ITEM_ID]

        db, cache = self.select_db_cache(data_type=data_type)
        item = cache.get_one(item_id=item_id)

        if item is None:
            return {"error message": "There is a error with the database / cache"}
        else:
            result = []
            for dataItem in item.data:
                heading = dataItem[Constants.HEADING]
                similar_set = get_similar_clauses(query=heading, clauses=3, item_id=item_id, database_ref=db,
                                                  cache_ref=cache)
                result.append({Constants.HEADING: heading, Constants.SIMILAR_SET: similar_set})

            return result

    def create_clusters(self, request):
        data_type = request.data[Constants.DATA_TYPE]
        no_of_clusters = request.data[Constants.NO_OF_CLUSTERS]

        db, cache = self.select_db_cache(data_type=data_type)

        return cluster_items(no_of_clusters=no_of_clusters, database_ref=db, cache_ref=cache)

    def create_pre_cluster(self, request):
        data_type = request.data[Constants.DATA_TYPE]
        no_of_clusters = request.data[Constants.NO_OF_CLUSTERS]
        pre_cluster_own_title = request.data[Constants.PRE_CLUSTER_OWN_TITLE]

        db, cache = self.select_db_cache(data_type=data_type)
        clusters = cluster_items(no_of_clusters=no_of_clusters, database_ref=db, cache_ref=cache)
        cluster_id = find_cluster_number(clusters, pre_cluster_own_title)
        return clusters[cluster_id]

    def select_db_cache(self, data_type):
        return get_cache_and_db(data_type=data_type, term_database=self.term_database, term_cache=self.term_cache,
                                policy_database=self.policy_database, policy_cache=self.policy_cache)
