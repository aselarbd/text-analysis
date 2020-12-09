"""
Utils functions for database handlers

"""


def detailsHelper(details):
    detailsList = []
    for obj in details:
        detailsList.append({"heading": obj.heading, "text": obj.text})
    return detailsList


# Singleton class for Database objects

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
