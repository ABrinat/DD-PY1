import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', newline='\n') :
    with open(filename) as file:
        list_1 = []
        is_head = True
        for line in file:
            lines = line.rstrip().split(newline)
            for current_line in lines:
                if is_head:
                    headings = current_line.split(delimiter)
                    is_head = False
                    continue
                list_1.append(dict(zip(headings, current_line.split(delimiter))))
    return list_1


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))