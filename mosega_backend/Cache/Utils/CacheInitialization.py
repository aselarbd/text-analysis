import Constants
from Cache.Utils.Utils import add_description_or_text_to_cache, add_corpus_cache


def init_cache(items, object_cache, heading_cache, text_cache, corpus_cache):
    init_object_cache(items=items, object_cache=object_cache)
    init_heading_cache(items=items, heading_cache=heading_cache)
    init_text_cache(items=items, text_cache=text_cache)
    init_corpus_cache(items=items, corpus_cache=corpus_cache)


def init_object_cache(items, object_cache):
    for item in items:
        object_cache[str(item.id)] = item


def init_heading_cache(items, heading_cache):
    for item in items:
        add_description_or_text_to_cache(item=item, field=Constants.HEADING, cache=heading_cache)


def init_text_cache(items, text_cache):
    for item in items:
        add_description_or_text_to_cache(item=item, field=Constants.TEXT, cache=text_cache)


def init_corpus_cache(items, corpus_cache):
    for item in items:
        add_corpus_cache(item=item, cache=corpus_cache)


def init_cache_without_corpus(items, object_cache, heading_cache, text_cache):
    init_object_cache(items=items, object_cache=object_cache)
    init_heading_cache(items=items, heading_cache=heading_cache)
    init_text_cache(items=items, text_cache=text_cache)

