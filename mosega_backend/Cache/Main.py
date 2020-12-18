from Cache.Utils.CacheInitialization import init_cache, init_cache_without_corpus
from Cache.Utils.CacheManipulation import add_item, get_all_items, get_one_item, delete_one_item, is_cache_empty, \
    is_item_in_cache
from Cache.Utils.CacheProcessing import get_all_heading_description_corpus_list, \
    get_heading_descriptions_corpus_except_one


def get_cache_reference(name):
    if name in Cache.cache_list:
        return Cache.cache_list[name]
    else:
        return Cache(name=name)


class Cache:
    cache_list = {}

    def __init__(self, name):
        if name not in Cache.cache_list:
            self.name = name
            self.object_cache = {}
            self.heading_cache = {}
            self.text_cache = {}
            self.corpus_cache = {}
            Cache.cache_list[name] = self

    def init_cache(self, items):
        init_cache(items=items, object_cache=self.object_cache, heading_cache=self.heading_cache,
                   text_cache=self.text_cache, corpus_cache=self.corpus_cache)

    def init_cache_without_corpus(self, items):
        return init_cache_without_corpus(items=items, object_cache=self.object_cache, heading_cache=self.heading_cache,
                                         text_cache=self.text_cache)

    def add(self, item):
        return add_item(item=item, object_cache=self.object_cache, heading_cache=self.heading_cache,
                        text_cache=self.text_cache)

    def get_one(self, item_id):
        return get_one_item(item_id=item_id, object_cache=self.object_cache)

    def get_all(self):
        return get_all_items(object_cache=self.object_cache)

    def is_empty(self):
        return is_cache_empty(object_cache=self.object_cache)

    def delete(self, item_id):
        return delete_one_item(item_id=item_id, object_cache=self.object_cache, heading_cache=self.heading_cache,
                               text_cache=self.text_cache, corpus_cache=self.corpus_cache)

    def is_item_contains(self, item_id):
        return is_item_in_cache(item_id=item_id, object_cache=self.object_cache)

    def get_heading_description_corpus_list(self):
        return get_all_heading_description_corpus_list(heading_cache=self.heading_cache, text_cache=self.text_cache,
                                                       corpus_cache=self.corpus_cache, object_cache=self.object_cache)

    def get_heading_description_corpus_list_except(self, item_id):
        return get_heading_descriptions_corpus_except_one(item_id=item_id, heading_cache=self.heading_cache,
                                                          text_cache=self.text_cache, corpus_cache=self.corpus_cache,
                                                          object_cache=self.object_cache)
