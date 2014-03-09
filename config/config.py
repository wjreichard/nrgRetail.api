__author__ = 'rike'


import configparser
import os
import logging.config

try:

    parser = configparser.ConfigParser()
    parser.read(os.path.dirname(__file__) + '\config.ini')

    #logging.config.fileConfig('config/logging.ini')

    # Initialize database, etc.
    enrollment_connection_string = parser.get('db_enrollment', 'connection_string')

    validation_schema = parser.get('validation', 'schema')

    #FLASK_DEBUG = parser.get('flask', 'debug', False)
    #server_port = int(parser.get('flask', 'server_port'))

except Exception as exception:
    print('Exception while configuring celery ERROR: {}'.format(str(exception)))
    raise
