import csv
import io
import json
import logging
import uuid
from domain import mmc_sku_lookup_repository as sku_repo


logger = logging.getLogger('api')


def csv_bytes_to_json(csv_bytes):

    logger.info("utility.csv_bytes_to_json(): start.")

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

    return json.dumps(result, sort_keys = True).replace('\\"', '')


def dict_to_csv(dictionary):

    logger.info("utility.dict_to_csv(): start.")

    output = io.StringIO()
    writer = csv.DictWriter(output,
                            fieldnames = sorted(dictionary[0].keys()),
                            delimiter = ',',
                            lineterminator = '\n',
                            quoting = csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(dictionary)
    result = output.getvalue()
    output.close()

    return result


def sku_generator():

    logger.info("utility.sku_generator(): start.")

    sku_uid = ''

    for _ in range(100):
        sku_uid = str(uuid.uuid4())[:13]
        if sku_repo.is_sku_in_use(sku_uid) is not True:
            break

    if sku_uid is '':
        raise Exception('utility.sku_generator(): After 100 tries, could not find an unused SKU')

    return sku_uid