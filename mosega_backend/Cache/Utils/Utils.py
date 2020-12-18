from sentence_transformers import SentenceTransformer
import Constants


def add_description_or_text_to_cache(item, field, cache):
    section_index = 1
    for data in item.data:
        cache[str(item.id) + '_' + str(section_index)] = data[field]
        section_index += 1


def generate_corpus(item):
    embedder = SentenceTransformer(Constants.SENTENCE_TRANSFORMER)
    heading_list = []
    for data in item.data:
        heading_list.append(data[Constants.HEADING])
    return embedder.encode(heading_list)


def add_corpus_cache(item, cache):
    corpus_set = generate_corpus(item=item)
    section_index = 1
    for corpus in corpus_set:
        cache[str(item.id) + '_' + str(section_index)] = corpus
        section_index += 1


def delete_cache_item(item_id, cache):
    for k in list(cache.keys()):
        if k.split("_")[0] == str(item_id):
            del cache[k]


def get_all_attribute_list(cache, with_key):
    attribute_list = []
    for cache_key in cache.keys():
        if with_key:
            attribute_list.append([cache_key, cache.get(cache_key)])
        else:
            attribute_list.append(cache.get(cache_key))
    return attribute_list


def get_all_except_one_attribute_list(item_id, cache, with_key):
    attribute_list = []
    for cache_key in cache.keys():
        if cache_key.split("_")[0] != str(item_id):
            if with_key:
                attribute_list.append([cache_key, cache.get(cache_key)])
            else:
                attribute_list.append(cache.get(cache_key))
    return attribute_list


def get_missing_object_ids(corpus_keys, total_keys):
    total_set = set()
    corpus_set = set()

    for k in total_keys:
        total_set.add(k.split("_")[0])
    for k in corpus_keys:
        corpus_set.add(k.split("_")[0])
    return total_set - corpus_set
