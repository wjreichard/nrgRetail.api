__author__ = 'rike'

import unittest
from domain import product_catalog_repository
from config import config


connection_string = config.enrollment_connection_string


class TestProductCatalogRepository(unittest.TestCase):

    def test_product_catalog_create(self):

        id = product_catalog_repository.product_catalog_create('boo', 'rike')
        self.assertEqual(id > 0, True)

    def test_product_catalog_event_create(self):

        id = product_catalog_repository.product_catalog_event_create(90, 'New', 'rike')
        self.assertEqual(id > 0, True)

    def test_product_catalog_failure_create(self):

        id = product_catalog_repository.product_catalog_failure_create(90, '{"Errors": "test"}', 'rike')
        self.assertEqual(id > 0, True)


if __name__ == '__main__':
    unittest.main()






