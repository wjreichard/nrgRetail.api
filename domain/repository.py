import pyodbc, sys
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
    with open_db_connection(enrollment_connection_string) as cursor:
        cursor.execute("""
                            SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{0}'
                                AND  TABLE_NAME = '{1}'".format(schema, table)
        """)
        return cursor.fetchone() is not None