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
