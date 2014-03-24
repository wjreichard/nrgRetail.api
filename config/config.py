import ast
import configparser
import os
import logging.config
import re


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

    columns = ast.literal_eval(parser.get('validation', 'columns'))

    # Initialize flask api
    server_port = int(parser.get('flask', 'server_port'))

    # Initialize logger
    logging.config.fileConfig(os.path.dirname(__file__) + '\logging.ini')

    # enums

    LockTypes = Enum(["Intro", "Contract", "Indexed"])
    ProductCatalogEventSlugs = Enum(["New", "Validated", "Invalidated", "Activated", "Deactivated"])
    TermsOfServiceTypes = Enum(["Fixed", "Variable", "Indexed"])

    # regex

    regex_currency = re.compile(r'^\$?(((\d{1,3},)+\d{3})|\d+)\.\d{2}$')
    regex_rate = re.compile(r'^(?=.*[1-9])\d*\.(\d{1,5})?$')

except Exception as exception:
    print('Exception while configuring ERROR: {}'.format(str(exception)))
    raise
