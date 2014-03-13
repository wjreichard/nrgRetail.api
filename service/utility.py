__author__ = 'rike'

import csv
import io
import json


def csv_bytes_to_json(csv_bytes):

    rows = csv_bytes.decode("utf-8").splitlines()

    csv = []
    headers = []

    for header in rows[0].split(','):
        headers.append(header)

    rows.remove(rows[0])

    for row in rows:
        row_items = {}
        for i, item in enumerate(row.split(',')):
            row_items[headers[i]] = item

        csv.append(row_items)

    return json.dumps(csv,  sort_keys=True).replace('\\"', '')


def dict_to_csv(dictionary):

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=dictionary[0].keys(),  delimiter=',', lineterminator='')
    writer.writerows(dictionary)
    print(output.getvalue())

    #f = io.BytesIO()
    #wrtr = csv.DictWriter(f, fieldnames="1 2".split())
    #wrtr.writerows('b{"1": "boo", "2": "foo"}'.encode('utf-8'))
    #print(f.getvalue())

    #csvwriter.writerow(dict((fn, fn) for fn in fieldnames))
    #for row in test_array:
    #     csvwriter.writerow(row)
    #print(test_file.getvalue())
    #test_file.close()



    #f = io.StringIO()
    #wrtr = csv.DictWriter(f, fieldnames="1 2 3".split())
    #wrtr.writerow({"1":30,"2":20,"3":10})
    #print(f.getvalue())

    #output = io.StringIO()
    #list(dictionary.keys()).
    #print(dictionary)
    #print(dictionary.keys())
    #d = {'name1': 'boo', 'name2': 'foo'}
    #print(d.keys())
    #writer = csv.DictWriter(output, d.keys())
    #writer.writeheader()
    #writer.writerow(d)
    #for key, value in dictionary.items():
    #    writer.writerow([key, value])
    #print('2')
    #print(output.getvalue())
    #print('3')

    return True #output