import Constants


def generate_new_item_id(database, db_type):
    if db_type == Constants.POLICY:
        return id_generator_helper(database, Constants.POLICY_ID)
    if db_type == Constants.TERM:
        return id_generator_helper(database, Constants.TERM_ID)


def id_generator_helper(db, field):
    if db.objects.values_list(field, flat=True).count() > 0:
        return max(db.objects.values_list(field, flat=True))+1
    else:
        return 1


def add_to_high_level_db(database, item_id, item_url, item_title, db_type):
    if db_type == Constants.POLICY:
        db_object = database(PolicyID=item_id, PolicyURL=item_url, PolicyTitle=item_title)
        db_object.save()
    if db_type == Constants.TERM:
        db_object = database(TermID=item_id, TermURL=item_url, TermTitle=item_title)
        db_object.save()


def add_to_details_db(database, item, item_id, db_type):
    if db_type == Constants.POLICY:
        section_id = 1
        for data in item.data:
            db_object = database(PolicyID=item_id, SectionID=section_id, heading=data[Constants.HEADING],
                                 text=data[Constants.TEXT])
            db_object.save()
            section_id += 1
    if db_type == Constants.TERM:
        section_id = 1
        for data in item.data:
            db_object = database(TermID=item_id, SectionID=section_id, heading=data[Constants.HEADING],
                                 text=data[Constants.TEXT])
            db_object.save()
            section_id += 1


def details_helper(items):
    details_list = []
    for item in items:
        details_list.append({Constants.HEADING: item.heading, Constants.TEXT: item.text})
    return details_list
