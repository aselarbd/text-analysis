from sentence_transformers import SentenceTransformer
import Constants


def add_description_or_text_to_cache(item, field, cache):
    section_index = 1
    for data in item.data:
        cache[str(item.id) + '_' + str(section_index)] = data[field]
        section_index += 1


def generate_corpus(item):
    embedder = SentenceTransformer('bert-base-nli-mean-tokens')
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


def get_all_attribute_list(cache):
    attribute_list = []
    for key in cache.keys():
        attribute_list.append([key, cache.get(key)])
    return attribute_list


def get_all_except_one_attribute_list(item_id, cache):
    attribute_list = []
    for key in cache.keys():
        if key.split("_")[0] != str(item_id):
            attribute_list.append([key, cache.get(key)])
    return attribute_list
