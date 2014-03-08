from service import product_validate

__author__ = 'rike'

import json


def create_products(csv_json):

    products = json.loads(csv_json)
    return json.dumps(do_create_products(products), sort_keys=True)

def do_create_products_1(products):
    schema_v1 = {
        'BrandSlug': {'is_valid_brand_slug': True, 'type': 'string'},
        'Channel': {'is_valid_channel': True, 'type': 'string'},
        'Extra': {'type': 'string'}
    }

    validator = product_validate.ProductValidator(schema_v1)

    def validated_products():
        for p in products:
            validator.validate(p)
            yield dict(p, Errors=validator.errors)


    return list(validated_products())

def do_create_products(products):
    schema_v1 = {
        'BrandSlug': {'is_valid_brand_slug': True, 'type': 'string'},
        'Channel': {'is_valid_channel': True, 'type': 'string'},
        'Extra': {'type': 'string'}
    }

    validator = product_validate.ProductValidator(schema_v1)

    def validated_products():
        for p in products:
            validator.validate(p)
            yield validator.errors

    errors = list(validated_products())

    return [dict(item[0], Errors = item[1]) for item in zip(products, errors)]
