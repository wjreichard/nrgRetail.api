import pyodbc
from config import config


connection_string = config.enrollment_connection_string


def get_brand_slugs():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT BrandSlug FROM epdata_brand WHERE brandSlug = 'nrg_residential'")

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
        channels.append(row.name.lower().translate(str.maketrans(' ', '_')))

    return channels

def get_premiseTypes():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT premiseType FROM premiseType")

    rows = cursor.fetchall()

    premiseTypes = []
    for row in rows:
        premiseTypes.append(row.premiseType)

    return premiseTypes

def get_partnerCodes():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT partnerCode FROM partners")

    rows = cursor.fetchall()

    partnerCodes = []
    for row in rows:
        partnerCodes.append(row.partnerCode)

    return partnerCodes

def get_promoCode():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT promoCode FROM promotions")

    rows = cursor.fetchall()

    promoCodes = []
    for row in rows:
        promoCodes.append(row.promoCode)

    return promoCodes

def get_vasCode():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT valueAddedServiceCode FROM valueAddedServices")

    rows = cursor.fetchall()

    vasCodes = []
    for row in rows:
        vasCodes.append(row.valueAddedServiceCode)

    return vasCodes

def get_pricePlans():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT u.UtilityCode, p.PricingPlan, p.Price FROM pricing_vw_PricingPlans p inner join Utilities u ON u.UtilityID = p.UtilityID")

    rows = cursor.fetchall()

    pricingPlans = []
    for row in rows:
        pricingPlans.append(row.pricingPlan)

    return pricingPlans

def get_utilityBrands():

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT u.UtilityCode, lower(u.UtilityAbbrev) as UtilityAbbrev, lower(u.State) as State, lower(u.Commodity) as Commodity, b.BrandSlug FROM vw_Utilities u INNER JOIN epdata_brandUtility bu ON bu.UtilityID = u.UtilityID INNER JOIN epdata_brand b ON bu.BrandID = b.BrandID")

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    utilitybrands = []
    for row in rows:
        utilitybrands.append(dict(zip(columns, row)))

    return utilitybrands