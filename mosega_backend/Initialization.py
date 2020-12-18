import Constants
from Cache.Main import get_cache_reference
from Database.Main import get_database_reference


def initialization():
    term_database = get_database_reference(Constants.TERM)
    term_cache = get_cache_reference(Constants.TERM)

    terms = term_database.get_all()
    term_cache.init_cache(items=terms)

    policy_database = get_database_reference(Constants.POLICY)
    policy_cache = get_cache_reference(Constants.POLICY)

    policies = policy_database.get_all()
    policy_cache.init_cache(items=policies)
