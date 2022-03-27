import csv
import json

with open('letters.csv', 'r') as f:
    output_dict = {}
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if row[0] in output_dict:
            output_dict[output_dict[row[0]]] = row[1]
        else:
            output_dict[row[0]] = row[1]

with open('letters.json', 'w') as f:
    json.dump(output_dict, f, ensure_ascii=False)