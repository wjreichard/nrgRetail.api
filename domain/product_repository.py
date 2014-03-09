__author__ = 'rike'

import pyodbc
from config import config


connection_string = config.enrollment_connection_string


def get_bland_slugs():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT BrandSlug FROM epdata_brand")

    rows = cursor.fetchall()

    brand_slugs = []
    for row in rows:
        brand_slugs.append(row.BrandSlug)

    return brand_slugs


def get_channels():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM apiChannels")

    rows = cursor.fetchall()

    channels = []
    for row in rows:
        channels.append(row.name)

    return channels
