import getpass
import json
import logging
from config import config
from decimal import *
from domain import product_catalog_repository as repo
from domain import mmc_sku_lookup_repository as sku_repo
from service import products_validate_individual_fields as field_validator
from service import products_validate_file as file_validator
from service import products_validate_multiple_fields as multi_field_validator
from service import products_validate_multiple_rows as multi_row_validator
from service import utility


logger = logging.getLogger('api')


def get_active_products_as_csv():
    logger.debug('product_catalog.create_products_from_json(): start.')
    logger.info('product catalog get_active products as csv initiated.')
    return utility.dict_to_csv(sku_repo.get_active_products())


def get_active_products_as_json():
    logger.debug('product_catalog.create_products_from_json(): start.')
    logger.info('product catalog get_active products as json initiated.')

    def decimal_default(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError

    return json.dumps(sku_repo.get_active_products(), default=decimal_default)


def activate_products_from_bytes(csv_bytes):
    logger.debug('product_catalog.activate_products_from_bytes(): start.')
    logger.info('product catalog activate initiated.')

    user = getpass.getuser()
    csv = csv_bytes.decode('utf-8')

    id = repo.product_catalog_insert(csv, user, True)
    repo.product_catalog_event_insert(id, config.ProductCatalogEventSlugs.New, user, True)

    products = validate(csv)

    if any(p['Errors'] != '{}' for p in products):
        post_errors(id, products, True)
        return utility.dict_to_csv(products)

    logger.info('product catalog activate validation successful.')
    repo.product_catalog_event_insert(id, config.ProductCatalogEventSlugs.Validated, user, True)

    sku_repo.activate_products(products, id, user, True)

    logger.info('product catalog activate complete.')
    repo.product_catalog_event_insert(id, config.ProductCatalogEventSlugs.Activated, user, True)

    return utility.dict_to_csv([{"Status": "Success"}])


def post_errors(product_catalog_id, errors, commit):
    logger.debug('product_catalog.post_errors(): start.')

    logger.warn('product_catalog.post_errors(): validate is invalid. ProductCatalogID: {}'
                .format(product_catalog_id))

    repo.product_catalog_event_insert(product_catalog_id,
                                      config.ProductCatalogEventSlugs.Invalidated,
                                      getpass.getuser(),
                                      commit)

    return repo.product_catalog_failure_insert(product_catalog_id,
                                               utility.dict_to_csv(errors),
                                               getpass.getuser(),
                                               commit)


def validate(csv):
    logger.debug('product_catalog.validate(): start.')
    logger.info('product catalog validate initiated.')

    errors = file_validator.validate(csv)
    if errors:
        return errors

    products = field_validator.validate(json.loads(utility.csv_to_json(csv)))
    products = multi_field_validator.validate(products)
    products = multi_row_validator.validate(products)

    return products


def validate_products_from_bytes(csv_bytes):
    logger.debug('product_catalog.validate_products_from_bytes(): start.')
    logger.info('product catalog validate products from bytes initiated.')

    results = validate(csv_bytes.decode('utf-8'))

    if any(e['Errors'] != '{}' for e in results):
        return utility.dict_to_csv(results)

    return utility.dict_to_csv([{"Status": "Success"}])