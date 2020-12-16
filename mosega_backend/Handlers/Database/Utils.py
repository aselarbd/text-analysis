"""
Utils functions for database handlers

"""


def detailsHelper(details):
    details_list = []
    for obj in details:
        details_list.append({"heading": obj.heading, "text": obj.text})
    return details_list


# Singleton class for Database objects

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
