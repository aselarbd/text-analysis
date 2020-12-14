import Constants
from Cache.Utils.Utils import add_description_or_text_to_cache, add_corpus_cache, delete_cache_item

"""
CRUD manipulations
"""


def add_item(item, object_cache, heading_cache, text_cache, corpus_cache):
    object_cache[str(item.id)] = item
    add_description_or_text_to_cache(item=item, field=Constants.HEADING, cache=heading_cache)
    add_description_or_text_to_cache(item=item, field=Constants.TEXT, cache=text_cache)
    add_corpus_cache(item=item, cache=corpus_cache)
    return True


def get_all_items(object_cache):
    return object_cache.values()


def get_one_item(item_id, object_cache):
    return object_cache.get(str(item_id))


def delete_all_items(object_cache, heading_cache, text_cache, corpus_cache):
    for one_item in object_cache.values():
        delete_one_item(item_id=one_item['id'], heading_cache=heading_cache, text_cache=text_cache,
                        corpus_cache=corpus_cache)


def delete_one_item(item_id, object_cache, heading_cache, text_cache, corpus_cache):
    del object_cache[str(item_id)]
    delete_cache_item(item_id=item_id, cache=heading_cache)
    delete_cache_item(item_id=item_id, cache=text_cache)
    delete_cache_item(item_id=item_id, cache=corpus_cache)
    return True


def is_cache_empty(object_cache):
    if len(object_cache.keys()) == 0:
        return True
    else:
        return False
