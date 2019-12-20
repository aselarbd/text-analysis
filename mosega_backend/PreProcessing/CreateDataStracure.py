import re


def create_data_structure(unstructured_string):
    lines = unstructured_string.split("\n")
    patten = re.compile("#")

    data_structure = {}

    heading_list = list(filter(patten.match, lines))
    no_of_headings = len(heading_list)

    position_tracker = [0] * 10

    element_count = 0
    position_holder = 'content'

    no_of_hash_list = [0] * no_of_headings
    heading_start_index = [0] * no_of_headings
    heading_end_index = [0] * no_of_headings

    for i in range(no_of_headings):
        no_of_hash_list[i] = heading_list[i].count('#')
        heading_start_index[i] = lines.index(heading_list[i])

        normalize = no_of_hash_list[i] - no_of_hash_list[0] + 1
        if normalize < 0:
            no_of_hash_list[i] = 0
        else:
            no_of_hash_list[i] = normalize

    for i in range(no_of_headings - 1):
        heading_end_index[i] = heading_start_index[i + 1] - 1

    heading_end_index[-1] = len(lines) - 1

    for heading in heading_list:
        no_of_hash = heading.count('#')

        position_tracker[no_of_hash - 1] += 1
        add_zeros_to_left_of_list(position_tracker, no_of_hash)

        if element_count == 0:
            data_structure['heading'] = heading_list[0][heading_list[0].count('#'):].strip()
            data_structure['text'] = ''.join(lines[heading_start_index[0] + 1:heading_end_index[0]])
            data_structure['content'] = []
            element_count += 1
        else:

            inner_json = {
                'heading': heading_list[element_count][heading_list[element_count].count('#'):].strip(),
                'text': ''.join(lines[heading_start_index[element_count] + 1:heading_end_index[element_count]]),
                'content': []
            }
            element_count += 1

            filling_level = get_filling_level(position_tracker)

            # TODO More testing and improve for more levels

            if filling_level == 1:
                data_structure[position_holder].append(inner_json)
            elif filling_level == 2:
                data_structure[position_holder][position_tracker[filling_level-1]-1][position_holder].append(inner_json)
            elif filling_level == 3:
                data_structure[position_holder][position_tracker[filling_level-2]-1][position_holder][position_tracker[filling_level - 1] - 1][position_holder].append(
                    inner_json)

    return data_structure


def add_zeros_to_left_of_list(position_list, position):
    for i in range(len(position_list)):
        if i >= position:
            position_list[i] = 0


def get_filling_level(position_tracker):
    for i in range(len(position_tracker)):
        if position_tracker[i] == 0:
            return i -1