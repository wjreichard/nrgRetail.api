__author__ = 'rike'

import unittest
from domain import product_catalog_repository


class TestProductCatalogRepository(unittest.TestCase):

    def test_product_catalog_create(self):

        product_catalog_repository.product_catalog_create('boo', 'rike')
        self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()






