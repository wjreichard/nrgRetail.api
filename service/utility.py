import csv
import io
import json
import logging


logger = logging.getLogger('api')


def csv_to_json(csv):
    logger.debug("utility.csv_to_json(): start.")

    rows = [r for r in csv.splitlines() if r]

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
    logger.debug("utility.dict_to_csv(): start.")

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