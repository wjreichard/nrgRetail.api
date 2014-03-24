import ast, logging
from config import config
from service import individual_product_validator as field_validator


logger = logging.getLogger('api')


def validate(products):
    logger.debug('products_validate_individual_fields.validate(): start.')

    schema = ast.literal_eval(config.validation_schema)
    validator = field_validator.ProductValidator(schema)

    def validated_products():
        for p in products:
            validator.validate(p)
            yield dict(p, Errors=str(validator.errors))

    return list(validated_products())