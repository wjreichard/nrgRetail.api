__author__ = 'rike'

import pyodbc


class Repository():


    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER=epdbdev01;DATABASE=epdata0137;Trusted_Connection=yes;'


    def get_bland_slugs(self):

        connection = pyodbc.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT BrandSlug FROM brand")

        rows = cursor.fetchall()

        brand_slugs = []
        for row in rows:
            brand_slugs.append(row.BrandSlug)

        return brand_slugs
