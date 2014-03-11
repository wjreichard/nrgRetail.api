__author__ = 'rike'

import unittest
import pyodbc
from config import config
from domain import product_repository

connection_string = config.enrollment_connection_string


class TestProductRepository(unittest.TestCase):

    def test_can_read_from_brand_table(self):

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT TOP 1 BrandSlug FROM epdata_brand WHERE brandslug = 'nrg_residential'")
        rows = cursor.fetchall()

        self.assertEqual(rows[0][0], 'nrg_residential')


    def test_can_read_from_channel_view(self):

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT TOP 1 name FROM apiChannels WHERE name = 'web'")
        rows = cursor.fetchall()

        self.assertEqual(rows[0][0].lower(), 'web')

if __name__ == '__main__':
    unittest.main()




