__author__ = 'rike'


import configparser
import os
import logging.config


class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


try:

    parser = configparser.ConfigParser()
    parser.read(os.path.dirname(__file__) + '\config.ini')

    # Initialize database
    enrollment_connection_string = parser.get('db_enrollment', 'connection_string')

    validation_schema = parser.get('validation', 'schema')

    # Initialize flask api
    server_port = int(parser.get('flask', 'server_port'))

    # Initialize logger
    logging.config.fileConfig(os.path.dirname(__file__) + '\logging.ini')

    # enums

    ProductCatalogEventSlugs = Enum(["New", "Validated", "Invalidated", "Activated", "Deactivated"])


except Exception as exception:
    print('Exception while configuring ERROR: {}'.format(str(exception)))
    raise
