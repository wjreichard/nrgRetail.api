__author__ = 'rike'

import pyodbc

connection_string = 'DRIVER={SQL Server};SERVER=epdbdev01;DATABASE=enrollment0137;Trusted_Connection=yes;'


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
