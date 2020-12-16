import Constants


def get_all_headings_from_db(details_db, db_type):
    headings_list = []
    if db_type == Constants.POLICY:
        policies = details_db.objects.order_by(Constants.POLICY_ID)

        for policy in policies:
            headings_list.append([str(policy.PolicyID) + '_' + str(policy.SectionID), policy.heading])

        return headings_list
    if db_type == Constants.TERM:
        terms = details_db.objects.order_by(Constants.TERM_ID)

        for term in terms:
            headings_list.append([str(term.TermID) + '_' + str(term.SectionID), term.heading])

        return headings_list


def get_all_description_from_db(details_db, db_type):
    description_list = []
    if db_type == Constants.POLICY:
        policies = details_db.objects.order_by(Constants.POLICY_ID)

        for policy in policies:
            description_list.append([str(policy.PolicyID) + '_' + str(policy.SectionID), policy.text])

        return description_list

    if db_type == Constants.TERM:
        terms = details_db.objects.order_by(Constants.TERM_ID)

        for term in terms:
            description_list.append([str(term.TermID) + '_' + str(term.SectionID), term.text])

        return description_list


def get_all_headings_and_descriptions_from_db(details_db, db_type):
    descriptions = get_all_description_from_db(details_db=details_db, db_type=db_type)
    headings = get_all_headings_from_db(details_db=details_db, db_type=db_type)
    return headings, descriptions
