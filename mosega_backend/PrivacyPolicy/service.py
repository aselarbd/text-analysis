from urllib.parse import urlparse

import Constants
from Cache.Main import get_cache_reference
from Database.Main import get_database_reference
from PreProcessing import PreProcessing
from PrivacyPolicy.serializer import Policy, PolicySerializer
from Shared.SharedFunctions import generate_cache

database = get_database_reference(Constants.POLICY)
cache = get_cache_reference(Constants.POLICY)


def get_all_policies():
    if cache.is_empty():
        policies = database.get_all()
        cache.init_cache_without_corpus(items=policies)
    else:
        policies = cache.get_all()
    serializer = PolicySerializer(policies, many=True)
    return serializer.data


def post_policy(request):
    policy_data = PreProcessing.getPolicy(request.data['url'])
    policy_title = urlparse(request.data['url']).hostname.split(".")[1]
    policy_url = request.data['url']
    policy = Policy(title=policy_title, url=policy_url, data=policy_data)
    policy_id = database.add_item(policy)
    policy.id = policy_id

    generate_cache(cache_ref=cache, database_ref=database)
    cache.add(item=policy)

    serializer = PolicySerializer(policy)
    return serializer.data


def get_one_policy(policy_id):
    generate_cache(cache_ref=cache, database_ref=database)
    policy = cache.get_one(item_id=policy_id)

    if policy:
        serializer = PolicySerializer(policy)
        return serializer.data
    else:
        policy = database.get_one(item_id=policy_id)
        if policy:
            cache.add(item=policy)
            serializer = PolicySerializer(policy)
            return serializer.data
        else:
            return {"error message": "requested policy not found in the database"}


def delete_one_policy(policy_id):
    generate_cache(cache_ref=cache, database_ref=database)
    is_deleted = database.delete_one(item_id=policy_id)

    if is_deleted and cache.is_item_contains(item_id=policy_id):
        cache.delete(item_id=policy_id)
        return {"success": "Deleted successfully"}
    return {"error message": "requested policy not found in the database"}
