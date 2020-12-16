from urllib.parse import urlparse

import Constants
from Cache.Main import get_cache_reference
from Database.Main import get_database_reference
from PreProcessing import PreProcessing
from Shared.SharedFunctions import generate_cache
from TermsAndConditions.serializer import Term, TermSerializer

database = get_database_reference(Constants.TERM)
cache = get_cache_reference(Constants.TERM)


def get_all_terms():
    if cache.is_empty():
        terms = database.get_all()
        cache.init_cache(items=terms)
    else:
        terms = cache.get_all()
    serializer = TermSerializer(terms, many=True)

    return serializer.data


def post_term(request):
    term_data = PreProcessing.getTerm(request.data['url'])
    term_title = urlparse(request.data['url']).hostname.split(".")[1]
    term_url = request.data['url']
    term = Term(title=term_title, url=term_url, data=term_data)
    term_id = database.add_item(item=term)
    term.id = term_id

    generate_cache(database_ref=database, cache_ref=cache)
    cache.add(item=term)

    serializer = TermSerializer(term)
    return serializer.data


def get_one_term(term_id):
    generate_cache(cache_ref=cache, database_ref=database)
    term = cache.get_one(item_id=term_id)

    if term:
        serializer = TermSerializer(term)
        return serializer.data
    else:
        term = database.get_one(item_id=term_id)
        if term:
            cache.add(item=term)
            serializer = TermSerializer(term)
            return serializer.data
        else:
            return {"error message": "requested term not found in the database"}


def delete_one_term(term_id):
    generate_cache(cache_ref=cache, database_ref=database)
    is_deleted = database.delete_one(item_id=term_id)

    if is_deleted and cache.is_item_contains(item_id=term_id):
        cache.delete(item_id=term_id)
        return {"success": "Deleted successfully"}
    return {"error message": "requested term not found in the database"}
