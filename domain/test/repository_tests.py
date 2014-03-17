import unittest
from domain import repository


class TestRepository(unittest.TestCase):

    def test_table_exists(self):

        self.assertEqual(repository.is_table("dbo", "mmc_sku_lookup"), True)

    def test_table_does_not_exists(self):

        self.assertEqual(repository.is_table("dbo", "__foo__"), False)


if __name__ == '__main__':
    unittest.main()





