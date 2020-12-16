import Constants
from Database.Utils.Utils import generate_new_item_id, add_to_high_level_db, add_to_details_db, details_helper
from PrivacyPolicy.serializer import Policy
from TermsAndConditions.serializer import Term


def add_item_to_db(item, high_level_db, details_db, db_type):
    item_id = generate_new_item_id(high_level_db, db_type)
    item_url = item.url
    item_title = item.title

    add_to_high_level_db(database=high_level_db, item_id=item_id, item_url=item_url, item_title=item_title,
                         db_type=db_type)
    add_to_details_db(database=details_db, item=item, item_id=item_id, db_type=db_type)

    return item_id


def get_all_items_from_db(high_level_db, details_db, db_type):
    item_list = []

    if db_type == Constants.POLICY:
        high_level_list = high_level_db.objects.order_by(Constants.POLICY_ID)

        for item in high_level_list:
            details = details_helper(items=details_db.objects.filter(PolicyID=item.PolicyID))
            policy = Policy(title=item.PolicyTitle, url=item.PolicyURL, data=details)
            policy.id = item.PolicyID
            item_list.append(policy)

    if db_type == Constants.TERM:
        high_level_list = high_level_db.objects.order_by(Constants.TERM_ID)

        for item in high_level_list:
            details = details_helper(items=details_db.objects.filter(TermID=item.TermID))
            term = Term(title=item.TermTitle, url=item.TermURL, data=details)
            term.id = item.TermID
            item_list.append(term)

    return item_list


def get_one_item_from_db(item_id, high_level_db, details_db, db_type):

    if db_type == Constants.POLICY:
        if high_level_db.objects.filter(PolicyID=item_id).count() > 0:
            high_level_item = high_level_db.objects.filter(PolicyID=item_id)
            details = details_helper(items=details_db.objects.filter(PolicyID=item_id))
            policy = Policy(title=high_level_item[0].PolicyTitle, url=high_level_item[0].PolicyURL, data=details)
            policy.id = item_id
            return policy

    if db_type == Constants.TERM:
        if high_level_db.objects.filter(TermID=item_id).count() > 0:
            high_level_item = high_level_db.objects.filter(TermID=item_id)
            details = details_helper(items=details_db.objects.filter(TermID=item_id))
            term = Term(title=high_level_item[0].TermTitle, url=high_level_item[0].TermURL, data=details)
            term.id = item_id
            return term

    return None


def delete_one_item_from_db(item_id, high_level_db, details_db, db_type):
    if db_type == Constants.POLICY:
        if high_level_db.objects.filter(PolicyID=item_id).count() > 0:
            policy = high_level_db.objects.filter(PolicyID=item_id)
            high_level_db.objects.filter(PolicyID=item_id).delete()
            details_db.objects.filter(PolicyID=item_id).delete()
            return policy
    if db_type == Constants.TERM:
        if high_level_db.objects.filter(TermID=item_id).count() > 0:
            term = high_level_db.objects.filter(TermID=item_id)
            high_level_db.objects.filter(TermID=item_id).delete()
            details_db.objects.filter(TermID=item_id).delete()
            return term
    return None


def is_db_empty(high_level_db):
    if high_level_db.objects.count() > 0:
        return False
    return True
