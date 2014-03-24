import unittest
from service import product_catalog
from service.test.product_catalog_test_fixtures import test_cases


class TestValidateProduct(unittest.TestCase):
    def test_create_products_from_bytes(self):
        csv_bytes = '"BrandSlug","Channel"\n"nrg_residential","AQ"\n"nrg_residential","AQ"'.encode('utf-8')
        expected = '"BrandSlug","Channel","Errors"\n"nrg_residential","AQ","{}"\n"nrg_residential","AQ","{}"\n'

        result = product_catalog.activate_products_from_bytes(csv_bytes)

        self.assertEqual(expected, result)


    def test_create_products_from_bytes_one_real_product(self):
        csv_bytes = ''
        expected = ''

        result = product_catalog.activate_products_from_bytes(csv_bytes)

        self.assertEqual(expected, result)


    def test_validate_products_multiple_rows(self):
        #products = [{"name": "boo"}, {"name": "foo"}, {"name": "123"}, {"name": "foo"}, {"name": "abc"}]
        products = [{'PartnerCode': 'nrr',
                     'Errors': {},
                     'BrandSlug': 'nrg_residential',
                     'PremiseType': 'residential',
                     'BundleSlug': 'variable',
                     'State': 'pa',
                     'BundleDescription': 'Basic Web Variable Plan',
                     'MerchandiseVesting': ''
                    }]

        result = product_catalog.validate_products_multiple_rows(products)
        print(result)
        #self.assertEqual(expected, result)


    def test_post_errors(self):
        errors = [{"message": "error"}]

        self.assertEqual(validator.post_errors(some_product_catalog_id_that_exists, errors, False) > 0, True)


if __name__ == '__main__':
    unittest.main()

