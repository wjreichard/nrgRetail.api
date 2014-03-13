__author__ = 'rike'

import pyodbc
import sys
from contextlib import closing
from domain import repository
from config import config


connection_string = config.enrollment_connection_string


def product_catalog_create(product_catalog, user):

    with repository.open_db_connection(connection_string, commit=True) as cursor:
        cursor.execute("""
                          INSERT INTO dbo.MMC_ProductCatalog (ProductCatalog, InsertUser)
                              OUTPUT INSERTED.ProductCatalogID
                              VALUES (?,?)
                    """, product_catalog, user)

        row = cursor.fetchone()
        return row[0]


def product_catalog_event_create(product_catalog_id, product_catalog_slug, user):

    with repository.open_db_connection(connection_string, commit=True) as cursor:
        cursor.execute("""
                        INSERT INTO dbo.MMC_ProductCatalogEvent (ProductCatalogID, ProductCatalogEventSlug, InsertUser)
                            OUTPUT INSERTED.ProductCatalogEventID
                              VALUES (?,?, ?)
                    """, product_catalog_id, product_catalog_slug, user)

        row = cursor.fetchone()
        return row[0]


def product_catalog_failure_create(product_catalog_id, errors, user):

    with repository.open_db_connection(connection_string, commit=True) as cursor:
        cursor.execute("""
                        INSERT INTO dbo.MMC_ProductCatalogFailure (ProductCatalogID, Errors, InsertUser)
                            OUTPUT INSERTED.ProductCatalogFailureID
                              VALUES (?,?, ?)
                    """, product_catalog_id, errors, user)

        row = cursor.fetchone()
        return row[0]