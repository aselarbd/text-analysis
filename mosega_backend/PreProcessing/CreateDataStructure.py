import re


def createDataStructure(unordered_data):
    """
    This function create structured, flat data structure for further processing
    """
    ordered_data = []
    split_data = unordered_data.split("\n")
    pattern = re.compile("^#")

    headings = list(filter(pattern.match, split_data))
    no_of_headings = len(headings)

    heading_index = [[0 for x in range(2)] for y in range(no_of_headings)]

    for i in range(no_of_headings):
        if i == no_of_headings - 1:
            heading_index[i][0] = split_data.index(headings[i])
            heading_index[i][1] = len(split_data) - 1
        else:
            heading_index[i][0] = split_data.index(headings[i])
            heading_index[i][1] = split_data.index(headings[i + 1]) - 1

    for heading in headings:
        index = headings.index(heading)
        json = {
            "heading": str(heading).replace("#","").lstrip(),
            "text": ''.join(split_data[heading_index[index][0] + 1: heading_index[index][1]])
        }
        ordered_data.append(json)
    return ordered_data
