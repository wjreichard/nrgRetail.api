__author__ = 'rike'

import unittest
from services.product import validate


class TestValidateProduct(unittest.TestCase):

    def test_validate_brand_slug(self):
        schema = {'BrandSlug': {'is_valid_brand_slug': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        brand_slug = {'BrandSlug': 'nrg_residential'}

        validator = validate.ProductValidator(schema)
        validator.allow_unknown = True

        assert(validator.validate(brand_slug) is True)


    def test_brand_slug_does_not_exist(self):
        schema = {'BrandSlug': {'is_valid_brand_slug': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        brand_slug = {'BrandSlug': 'foo'}

        validator = validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(brand_slug), False)


if __name__ == '__main__':
    unittest.main()

