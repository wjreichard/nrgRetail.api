__author__ = 'rike'

import json


class Converter():

    def csv_bytes_to_json(self, csv_bytes):
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