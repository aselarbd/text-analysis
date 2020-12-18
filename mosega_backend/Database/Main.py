import Constants
from PrivacyPolicy.models import PolicyDetails, PolicyHighLevel
from TermsAndConditions.models import TermHighLevel, TermDetails
from Database.Utils.DBManipulations import add_item_to_db, get_all_items_from_db, get_one_item_from_db, \
    delete_one_item_from_db, is_db_empty
from Database.Utils.DBProcessing import get_all_headings_from_db, get_all_description_from_db, \
    get_all_headings_and_descriptions_from_db


def get_database_reference(name):
    if name in Database.database_list:
        return Database.database_list[name]
    else:
        if name == Constants.POLICY:
            high_level = PolicyHighLevel
            details = PolicyDetails
            return Database(name=name, high_level=high_level, details=details)
        if name == Constants.TERM:
            high_level = TermHighLevel
            details = TermDetails
            return Database(name=name, high_level=high_level, details=details)


class Database:
    database_list = {}

    def __init__(self, name, high_level, details):
        if name not in Database.database_list:
            self.db_type = name
            self.high_level_db = high_level
            self.details_db = details
            Database.database_list[name] = self

    def add_item(self, item):
        return add_item_to_db(item=item, high_level_db=self.high_level_db, details_db=self.details_db,
                              db_type=self.db_type)

    def get_all(self):
        return get_all_items_from_db(high_level_db=self.high_level_db, details_db=self.details_db, db_type=self.db_type)

    def get_one(self, item_id):
        return get_one_item_from_db(item_id=item_id, high_level_db=self.high_level_db, details_db=self.details_db,
                                    db_type=self.db_type)

    def delete_one(self, item_id):
        return delete_one_item_from_db(item_id=item_id, high_level_db=self.high_level_db, details_db=self.details_db,
                                       db_type=self.db_type)

    def is_empty(self):
        return is_db_empty(high_level_db=self.high_level_db)

    def get_all_headings(self):
        return get_all_headings_from_db(details_db=self.details_db, db_type=self.db_type)

    def get_all_descriptions(self):
        return get_all_description_from_db(details_db=self.details_db, db_type=self.db_type)

    def get_all_headings_and_descriptions(self):
        return get_all_headings_and_descriptions_from_db(details_db=self.details_db, db_type=self.db_type)
