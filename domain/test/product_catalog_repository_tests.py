import unittest
from domain import product_catalog_repository as repo


class TestProductCatalogRepository(unittest.TestCase):
    def test_product_catalog_insert(self):
        identity = repo.product_catalog_insert('booxxx', 'rike', False)
        self.assertEqual(identity > 0, True)

    def test_product_catalog_event_create(self):
        identity = repo.product_catalog_event_insert(3, 'New', 'rike', False)
        self.assertEqual(identity > 0, True)

    def test_product_catalog_failure_create(self):
        identity = repo.product_catalog_failure_insert(3, '{"Errors": "test"}', 'rike', False)
        self.assertEqual(identity > 0, True)


if __name__ == '__main__':
    unittest.main()






