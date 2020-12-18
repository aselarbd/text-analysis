import Constants


def get_column(matrix, i):
    return [row[i] for row in matrix]


def get_headings_and_description_list(db, cache, item_id):
    if item_id is not None:
        headings, descriptions = cache.get_headings_and_description_without_one(item_id)
    else:
        headings, descriptions = cache.get_heading_and_description_list()

    if len(headings) == 0 or len(descriptions) == 0:
        headings, descriptions = db.getAllHeadingAndDescriptionList()
    return headings, descriptions


def get_headings_corpus(cache, corpus, embedder):
    current_headings_list = cache.get_all_headings_list()
    if len(corpus) < len(current_headings_list):
        new_headings = get_column(matrix=current_headings_list[len(corpus):len(current_headings_list)], i=1)
        return embedder.encode(new_headings)
    return None


def process_preparation(database, cache, without_id):
    if without_id is None:
        if cache.is_empty() is True:
            cache_update(cache_ref=cache, database_ref=database)
        return cache.get_heading_description_corpus_list()
    else:
        if cache.is_empty() is True:
            cache_update(cache_ref=cache, database_ref=database)
        return cache.get_heading_description_corpus_list_except(item_id=without_id)


def cache_update(cache_ref, database_ref):
    items = database_ref.get_all()
    cache_ref.init_cache_without_corpus(items=items)


def find_cluster_number(clusters, title):
    for i in range(len(clusters)):
        for item in clusters[i]:
            if item[Constants.HEADING] == title:
                return i


def get_cache_and_db(data_type, term_database, term_cache, policy_database, policy_cache):
    if data_type == Constants.TERM:
        db = term_database
        cache = term_cache
    else:
        db = policy_database
        cache = policy_cache
    return db, cache
