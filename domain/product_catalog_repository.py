__author__ = 'rike'

import pyodbc
from config import config

connection_string = config.enrollment_connection_string


def product_catalog_create(product_catalog, user):

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    boo = cursor.execute("""
                            INSERT INTO dbo.MMC_ProductCatalog (ProductCatalog, InsertUser)
                                OUTPUT INSERTED.ProductCatalogID
                                VALUES (?,?)
                        """, product_catalog, user)

    print('--------------------------------')
    print(boo)
    print('--------------------------------')

    connection.commit()

    return 0

