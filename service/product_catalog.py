from service import product_validate

__author__ = 'rike'

import csv
import json
import logging
import getpass
from config import config
from domain import product_catalog_repository
from service import utility


def create_products_from_bytes(csv_bytes):

    #event_slug = Enum(["New", "Validated", "Invalidated", "Activated", "Deactivated"])
    #print(event_slug.NEW)

    logger = logging.getLogger('api')
    logger.info("create_products_from_json: start.")

    product_catalog_id = product_catalog_repository.product_catalog_create(csv_bytes, getpass.getuser())
    product_catalog_repository.product_catalog_event_create(product_catalog_id, 'New', getpass.getuser())

    file_errors = validate_products_file(csv_bytes.decode('utf-8'))

    if len(file_errors) is not 0:
        errors_json = json.dumps(file_errors)
        logger.info("create_products_from_json: validate_products_file error encountered.")
        product_catalog_repository.product_catalog_event_create(product_catalog_id, 'Invalidated', getpass.getuser())
        product_catalog_repository.product_catalog_failure_create(product_catalog_id, errors_json, getpass.getuser())
        return errors_json

    csv_json = utility.csv_bytes_to_json(csv_bytes)
    products = json.loads(csv_json)

    pipeline = [validate_products_row, validate_products_multiple_rows]
    boo = [f(products) for f in pipeline]
    print(boo)

    return json.dumps(products, sort_keys=True)


def validate_products_file(products):
    errors = {}

    result = csv.Sniffer().sniff(products)
    if result.delimiter is not ',':
        errors = {"File Structure": "comma delimiter not found"}

    #print(boo.delimiter)
    #sanity check ... is this a csv ... with required headers?
    return errors


def validate_products_row(products):

    schema = json.loads(config.validation_schema)
    validator = product_validate.ProductValidator(schema)

    def validated_products():
        for p in products:
            validator.validate(p)
            yield dict(p, Errors=validator.errors)

    return list(validated_products())


def validate_products_multiple_rows(products):
    for p in products:
        for key in p.keys():
            print(key)
        #if 'Errors' in p:
        #    p['Errors']['rows'] = 'validate_products_multiple_rows error'
        #else:
        #    print('xxx')
        #    p['Errors'] = '[]'
        #    #p['Errors']['rows'] = 'first error'
        #print(p)
