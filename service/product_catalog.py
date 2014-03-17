import csv
import json
import logging
import getpass
from config import config
from domain import product_catalog_repository as repo
from domain import mmc_sku_lookup_repository as sku_repo
from service import product_validate
from service import utility


logger = logging.getLogger('api')


def get_active_products():

    logger.info('product_catalog.create_products_from_json(): start.')
    return utility.dict_to_csv(sku_repo.get_active_products())


def create_products_from_bytes(csv_bytes):

    logger.info('product_catalog.create_products_from_bytes(): start.')

    csv_string = csv_bytes.decode('utf-8')

    id = repo.product_catalog_insert(csv_string, getpass.getuser(), True)
    repo.product_catalog_event_insert(id, config.ProductCatalogEventSlugs.New, getpass.getuser(), True)

    file_errors = validate_products_file(csv_string)

    if len(file_errors) is not 0:
        logger.warn('product_catalog.create_products_from_bytes(): validate_products_file is invalid id: {}'.format(id))
        repo.product_catalog_event_insert(id, config.ProductCatalogEventSlugs.Invalidated, getpass.getuser(), True)
        errors_csv = utility.dict_to_csv(file_errors)
        repo.product_catalog_failure_insert(id, errors_csv, getpass.getuser(), True)
        return errors_csv
    print('1')
    print(utility.csv_bytes_to_json(csv_bytes))
    print('2')
    products = validate_products_individual_fields(json.loads(utility.csv_bytes_to_json(csv_bytes)))
    #products = validate_products_multiple_fields(products)
    #products = validate_products_multiple_rows(products)

    if any(p['Errors'] != {} for p in products):
        logger.info('product_catalog.create_products_from_bytes(): validation error(s) encountered.')
        repo.product_catalog_event_insert(id, config.ProductCatalogEventSlugs.Invalidated, getpass.getuser(), True)
        errors_csv = utility.dict_to_csv(products)
        repo.product_catalog_failure_insert(id, errors_csv, getpass.getuser(), True)
        return errors_csv
    else:
        logger.info('product_catalog.create_products_from_bytes: validation successful.')
        repo.product_catalog_event_insert(id, config.ProductCatalogEventSlugs.Validated, getpass.getuser(), True)

    mmc_sku_lookup_update(products, id)

    repo.product_catalog_event_insert(id, config.ProductCatalogEventSlugs.Activated, getpass.getuser(), True)

    return utility.dict_to_csv([{"Status": "Success"}])
    #return utility.dict_to_csv(sku_repo.mmc_sku_lookup_get_active())


    #pipeline = [validate_products_row,
    #            validate_products_multiple_rows]

    #result = [f(products) for f in pipeline]

    #return json.dumps(products, sort_keys=True)


def mmc_sku_lookup_update(products, product_category_id):

    logger.info('product_catalog.mmc_sku_lookup_update(): start.')

    deactivate_product_category_id = sku_repo.get_active_product_catalog_id()
    logger.info('product_catalog.mmc_sku_lookup_update(): deactivating product catalog id: {0}.'
               .format(deactivate_product_category_id))
    sku_repo.deactivate_products(deactivate_product_category_id, getpass.getuser(), True)

    for p in products:
        p["SKU"] = utility.sku_generator()
        logger.info('product_catalog.mmc_sku_lookup_update(): insert product SKU: {0}.'.format(p["SKU"]))
        sku_repo.insert_product(p, product_category_id, getpass.getuser(), True)


def validate_products_file(csv_string):

    logger.info('product_catalog.validate_products_file(): start.')

    errors = []

    result = csv.Sniffer().sniff(csv_string)

    if result.delimiter is not ',':
        errors = [{"Type": "File", "Message": "comma delimiter not found" }]

    #sanity check ... is this a csv ... with required headers?
    return errors


def validate_products_individual_fields(products):

    logger.info('product_catalog.validate_products_individual_fields(): start.')

    schema = json.loads(config.validation_schema)
    validator = product_validate.ProductValidator(schema)

    def validated_products():
        for p in products:
            validator.validate(p)
            yield dict(p, Errors=validator.errors)

    return list(validated_products())


def validate_products_multiple_fields(products):

    logger.info('product_catalog.validate_products_multiple_fields(): start.')

    schema = json.loads(config.multivalidation_schema)
    validator = product_validate.ProductValidator(schema)

    def validated_products():
        for p in products:
            validator.validate(p)
            yield dict(p, Errors=validator.errors)

    return list(validated_products())


def validate_products_multiple_rows(products):

    logger.info('product_catalog.validate_products_multiple_rows(): start.')
    return products
