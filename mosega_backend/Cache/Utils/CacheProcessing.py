from Cache.Utils.Utils import get_all_attribute_list, get_all_except_one_attribute_list, get_missing_object_ids, \
    add_corpus_cache


def get_all_heading_description_corpus_list(heading_cache, text_cache, corpus_cache, object_cache):
    headings = get_all_attribute_list(cache=heading_cache, with_key=True)
    texts = get_all_attribute_list(cache=text_cache, with_key=True)

    missing_keys = get_missing_object_ids(corpus_keys=corpus_cache.keys(), total_keys=heading_cache.keys())
    for key in missing_keys:
        add_corpus_cache(cache=corpus_cache, item=object_cache[key])

    corpus = get_all_attribute_list(cache=corpus_cache, with_key=False)
    return headings, texts, corpus


def get_heading_descriptions_corpus_except_one(item_id, heading_cache, text_cache, corpus_cache, object_cache):
    headings = get_all_except_one_attribute_list(item_id=item_id, cache=heading_cache, with_key=True)
    texts = get_all_except_one_attribute_list(item_id=item_id, cache=text_cache, with_key=True)

    missing_keys = get_missing_object_ids(corpus_keys=corpus_cache.keys(), total_keys=heading_cache.keys())
    for key in missing_keys:
        if key != item_id:
            add_corpus_cache(cache=corpus_cache, item=object_cache[key])

    corpus = get_all_except_one_attribute_list(item_id=item_id, cache=corpus_cache, with_key=False)
    return headings, texts, corpus
