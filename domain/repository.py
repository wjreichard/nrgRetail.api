__author__ = 'rike'


import pyodbc
import sys
from contextlib import contextmanager
from config import config


enrollment_connection_string = config.enrollment_connection_string

@contextmanager
def open_db_connection(connection_string, commit=False):
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    try:
        yield cursor
    except pyodbc.DatabaseError as err:
        error, = err.args
        sys.stderr.write(error.message)
        cursor.execute("ROLLBACK")
        raise err
    else:
        if commit:
            cursor.execute("COMMIT")
        else:
            cursor.execute("ROLLBACK")
    finally:
        connection.close()


def is_table(schema, table):

    sql = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{0}' AND  TABLE_NAME = '{1}'" \
        .format(schema, table)

    with open_db_connection(enrollment_connection_string) as cursor:
        cursor.execute(sql)
        return cursor.fetchone() is not None


#def create_mmc_product_catalog_table():

#    sql = """
#            SET ANSI_NULLS ON

#            SET QUOTED_IDENTIFIER ON

#            SET ANSI_PADDING ON

#            CREATE TABLE [dbo].[MMC_ProductCatalog](
#                [ProductCatalogID] [int] IDENTITY(1,1) NOT NULL,
#                [ProductCatalog] [varchar](max) NOT NULL,
#                [InsertDT] [datetime] NOT NULL,
#                [InsertUser] [varchar](32) NOT NULL,
#                CONSTRAINT [PK_MC_ProductCatalog] PRIMARY KEY CLUSTERED
#                (
#                    [ProductCatalogID] ASC
#                )
#                WITH
#                (
#                    PAD_INDEX  = OFF,
#                    STATISTICS_NORECOMPUTE  = OFF,
#                    IGNORE_DUP_KEY = OFF,
#                    ALLOW_ROW_LOCKS  = ON,
#                    ALLOW_PAGE_LOCKS  = ON
#                ) ON [PRIMARY]
#            ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

#            SET ANSI_PADDING OFF

#            ALTER TABLE [dbo].[MMC_ProductCatalog] ADD  CONSTRAINT [DF_MMC_ProductCatalog_InsertDT]
#                DEFAULT (getdate()) FOR [InsertDT]

#            ALTER TABLE [dbo].[MMC_ProductCatalog] ADD  CONSTRAINT [DF_MMC_ProductCatalog_InsertUser]
#                DEFAULT ([dbo].[fn_CurUser]()) FOR [InsertUser]
#    """

#    connection = pyodbc.connect(connection_string)
#    cursor = connection.cursor()
#    cursor.execute(sql)

#    return True