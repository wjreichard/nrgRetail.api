import csv, getpass, logging
from config import config
from domain import product_catalog_repository as repo
from service import utility


logger = logging.getLogger('api')


def validate(csv):
    logger.debug('product_validate_file.validate(): start.')

    errors = []
    is_csv(csv, errors)

    if errors:
        return errors

    are_all_columns_expected(csv, errors)
    are_any_columns_missing(csv, errors)

    return errors


def is_csv(csv_string, errors):
    logger.debug('product_validate_file.is_csv(): start.')

    result = csv.Sniffer().sniff(csv_string)

    if result.delimiter is not ',':
        errors.append({"Errors": {"Type": "File", "Message": "comma delimiter not found"}})

    return errors


def are_all_columns_expected(csv_string, errors):
    logger.debug('product_validate_file.are_all_columns_expected(): start.')

    rows = csv_string.splitlines()
    fields = rows[0].split(',')

    for f in fields:
        if not f.replace('"', '').strip() in config.columns:
            errors.append({"Errors": {"Type": "File", "Message": "{0} not a valid column.".format(f)}})

    return errors


def are_any_columns_missing(csv_string, errors):
    logger.debug('product_validate_file.are_any_columns_missing(): start.')

    rows = csv_string.splitlines()
    fields = rows[0].split(',')

    for c in config.columns:

        if not c in [f.replace('"', '').strip() for f in fields]:
            errors.append({"Errors": {"Type": "File", "Message": "{0} column is missing.".format(c)}})

    return errors



