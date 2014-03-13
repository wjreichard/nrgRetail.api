__author__ = 'rike'

import csv
import io
import json


def csv_bytes_to_json(csv_bytes):

    rows = csv_bytes.decode("utf-8").splitlines()

    result = []
    headers = []

    for header in rows[0].split(','):
        headers.append(header)

    rows.remove(rows[0])

    for row in rows:
        row_items = {}
        for i, item in enumerate(row.split(',')):
            row_items[headers[i]] = item

        result.append(row_items)

    return json.dumps(result, sort_keys=True).replace('\\"', '')


def dict_to_csv(dictionary):

    output = io.StringIO()
    writer = csv.DictWriter(output,
                            fieldnames=sorted(dictionary[0].keys()),
                            delimiter=',',
                            lineterminator='\n',
                            quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(dictionary)
    result = output.getvalue()
    output.close()

    return result