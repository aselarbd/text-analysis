"""
Utils functions for database handlers

"""


def detailsHelper(details):
    detailsList = []
    for obj in details:
        detailsList.append({"heading": obj.heading, "text": obj.text})
    return detailsList
