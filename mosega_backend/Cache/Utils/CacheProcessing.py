from Cache.Utils.Utils import get_all_attribute_list, get_all_except_one_attribute_list


def get_all_heading_description_corpus_list(heading_cache, text_cache, corpus_cache):
    headings = get_all_attribute_list(cache=heading_cache)
    texts = get_all_attribute_list(cache=text_cache)
    corpus = get_all_attribute_list(cache=corpus_cache)
    return headings, texts, corpus


def get_heading_descriptions_corpus_except_one(item_id, heading_cache, text_cache, corpus_cache):
    headings = get_all_except_one_attribute_list(item_id=item_id, cache=heading_cache)
    texts = get_all_except_one_attribute_list(item_id=item_id, cache=text_cache)
    corpus = get_all_except_one_attribute_list(item_id=item_id, cache=corpus_cache)
    return headings, texts, corpus
