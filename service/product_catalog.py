from service import product_validate

__author__ = 'rike'

import csv
import json
import logging
import getpass
from config import config
from domain import product_catalog_repository
from service import utility


logger = logging.getLogger('api')


def create_products_from_bytes(csv_bytes):

    logger.info("create_products_from_json: start.")

    product_catalog_id = product_catalog_repository.product_catalog_create(csv_bytes, getpass.getuser())
    product_catalog_repository.product_catalog_event_create(product_catalog_id,
                                                            config.ProductCatalogEventSlugs.New,
                                                            getpass.getuser())

    file_errors = validate_products_file(csv_bytes.decode('utf-8'))

    if len(file_errors) is not 0:
        errors_csv = utility.dict_to_csv(file_errors)
        logger.info("create_products_from_json: validate_products_file error encountered. {}".format(file_errors))
        product_catalog_repository.product_catalog_event_create(product_catalog_id,
                                                                config.ProductCatalogEventSlugs.Invalidated,
                                                                getpass.getuser())
        product_catalog_repository.product_catalog_failure_create(product_catalog_id, errors_csv, getpass.getuser())
        return errors_csv

    csv_json = utility.csv_bytes_to_json(csv_bytes)
    products = json.loads(csv_json)

    products = validate_products_row(products)

    if any(p['Errors'] != {} for p in products):
        errors_csv = utility.dict_to_csv(products)
        logger.info("create_products_from_json: validate_products_row error encountered. {}".format(products))
        product_catalog_repository.product_catalog_event_create(product_catalog_id,
                                                                config.ProductCatalogEventSlugs.Invalidated,
                                                                getpass.getuser())
        product_catalog_repository.product_catalog_failure_create(product_catalog_id, errors_csv, getpass.getuser())
        return errors_csv
    else:
        product_catalog_repository.product_catalog_event_create(product_catalog_id,
                                                                config.ProductCatalogEventSlugs.Validated,
                                                                getpass.getuser())

    return utility.dict_to_csv(products)

    #pipeline = [validate_products_row,
    #            validate_products_multiple_rows]

    #result = [f(products) for f in pipeline]
    #print(result)

    #return json.dumps(products, sort_keys=True)


def validate_products_file(csv_string):
    errors = []

    result = csv.Sniffer().sniff(csv_string)

    if result.delimiter is not ',':
        errors = [{"Type": "File", "Message": "comma delimiter not found" }]

    #sanity check ... is this a csv ... with required headers?
    return errors


def validate_products_row(products): #this is really only validation of single columns right now

    schema = json.loads(config.validation_schema)
    validator = product_validate.ProductValidator(schema)

    def validated_products():
        for p in products:
            validator.validate(p)
            yield dict(p, Errors=validator.errors)

    return list(validated_products())

def validate_products_intra_row(products): #this includes validation of multiple columns within a row (combined validation)

    schema = json.loads(config.multivalidation_schema)
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
