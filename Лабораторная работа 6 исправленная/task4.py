import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', newline='\n'):
    with open(filename) as file:
        list_1 = []
        if newline == '\n':
            headings = file.readline().rstrip('\n').split(delimiter)
            for line in file:
                list_1.append(dict(zip(headings, line.rstrip('\n').split(delimiter))))
        else:
            line = file.readline().rstrip('\n')
            lines = line.split(newline)
            headings = lines[0].split(delimiter)
            for i in range(1, len(lines)):
                list_1.append(dict(zip(headings, lines[i].split(delimiter))))
    return list_1


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
