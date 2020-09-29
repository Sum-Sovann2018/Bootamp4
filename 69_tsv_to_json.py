import csv, json, os

def tsv_to_json(tsvfile, jsonfile):
    data = {}

    if os.path.exists(tsvfile):

        with open(tsvfile) as file:

            reader = csv.DictReader(file, delimiter = '\t')
            data = list(reader)

        with open(jsonfile, 'w') as jsonf:

            jsonf.write(json.dumps(data, indent = 4))

        return 1

    else:
        return 0

print(tsv_to_json('second','bc_test.json'))