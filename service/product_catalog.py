from service import product_validate

__author__ = 'rike'

import json
import logging
from config import config


def create_products_from_json(csv_json):

    logger = logging.getLogger('api')
    logger.info("create_products_from_json")

    products = json.loads(csv_json)

    products = validate_products_file(products)
    products = validate_products_row(products)
    products = validate_products_multiple_rows(products)

    return json.dumps(products, sort_keys=True)


def validate_products_file(products):

    return products


def validate_products_row(products):

    schema = json.loads(config.validation_schema)
    validator = product_validate.ProductValidator(schema)

    def validated_products():
        for p in products:
            validator.validate(p)
            yield dict(p, Errors=validator.errors)

    return list(validated_products())


def validate_products_multiple_rows(products):

    return products
