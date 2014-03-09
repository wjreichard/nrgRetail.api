__author__ = 'rike'

import unittest
from service import product_catalog
from service.test.product_catalog_test_fixtures import test_cases


class TestValidateProduct(unittest.TestCase):

    def test_create_products(self):

        products = [{"BrandSlug": "energyplus", "Channel": "web"}, {"BrandSlug": "nrg_residential", "Channel": "Retention"}]
        expected = [{"BrandSlug": "energyplus", "Channel": "web", "Errors": {}}, {"BrandSlug": "nrg_residential", "Channel": "Retention", "Errors": {}}]

        result = product_catalog.validate_products_row(products)

        self.assertEqual(result, expected)

    #def test_create_products_multiple_valid_products(self):

    #    products = '[{"BrandSlug": "energyplus", "Channel": "web"}, ' \
    #               '{"BrandSlug": "nrg_residential", "Channel": "Retention"}]'
    #    expected = '[{"BrandSlug": "energyplus", "Channel": "web", "Errors": {}}, {"BrandSlug": "nrg_residential", "Channel": "Retention", "Errors": {}}]'
    #    result = product_catalog.create_products_from_json(products)

    #    assert(True is True)

    #def test_do_create_products_from_fixtures(self):

    #    for item in test_cases:
    #        result = product_catalog.validate_individual_product_fields(item['products'])
    #        self.assertEqual(result, item['expected'])

    #def test_do_create_products_from_fi(self):
    #    def mssql():
    #        return "MIcorsql"

    #    def mysql():
    #        return "unix"

    #    repository = mssql

    #    print ("hello %s " % repository())

if __name__ == '__main__':
    unittest.main()

