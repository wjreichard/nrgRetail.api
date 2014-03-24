import ast, logging


logger = logging.getLogger('api')


def validate(products):
    logger.debug('product_validate_multiple_rows.validate(): start.')

    return check_for_duplicates(products)


def check_for_duplicates(products):
    logger.debug('product_validate_multiple_rows.check_for_duplicates(): start.')

    # check for duplicates
    unique_products = [dict(t) for t in set([tuple(p.items()) for p in products])]

    diff = products

    for p in unique_products:
        diff.remove(p)

    for p in diff:
        e = ast.literal_eval(p['Errors'])
        e.update({"Row": "duplicate"})
        p['Errors'] = str(e)
        unique_products.append(p)

    return unique_products

