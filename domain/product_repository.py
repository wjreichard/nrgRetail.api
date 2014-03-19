import logging, pyodbc
from config import config
from domain import repository


connection_string = config.enrollment_connection_string
logger = logging.getLogger('api')


def does_active_offer_charge_id_exist(offer_charge_id):

    logger.info('product_repository.does_active_offer_charge_id_exist(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute("""
                            SELECT OfferChargeID from apiOfferCharges
                            WHERE OfferChargeID = '{0}' AND
                            Active = 1
                       """.format(offer_charge_id))

        return cursor.fetchone() is not None


def does_valid_offer_code_exist(offer_code):

    logger.info('product_repository.does_valid_offer_code_exist(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute("""
                            SELECT OfferCode from apiOffers
                            WHERE OfferCode = '{0}' AND
                            ValidThrough IS NULL OR ValidThrough >= GETDATE()
                       """.format(offer_code))

        return cursor.fetchone() is not None


def get_brand_slugs():

    logger.info('product_repository.get_brand_slugs(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('SELECT BrandSlug FROM epdata_brand WHERE brandSlug = \'nrg_residential\'')

    rows = cursor.fetchall()

    brand_slugs = []
    for row in rows:
        brand_slugs.append(row.BrandSlug)

    return brand_slugs


def get_channels():

    logger.info('product_repository.get_channels(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM apiChannels')

    rows = cursor.fetchall()

    channels = []
    for row in rows:
        channels.append(row.name.lower().translate(str.maketrans(' ', '_')))

    return channels


def get_partner_codes():

    logger.info('product_repository.get_partner_codes(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('SELECT partnerCode FROM partners')

    rows = cursor.fetchall()

    product_codes = []
    for row in rows:
        product_codes.append(row.partnerCode)

    return product_codes


def get_premise_types():

    logger.info('product_repository.get_premise_types(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('SELECT premiseType FROM premiseType')

    rows = cursor.fetchall()

    premise_types = []
    for row in rows:
        premise_types.append(row.premiseType)

    return premise_types


def get_price_plans():

    logger.info('product_repository.get_price_plans(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("""
                        SELECT
                            u.UtilityCode,
                            p.PricingPlan,
                            p.Price
                        FROM pricing_vw_PricingPlans AS p
                        INNER JOIN Utilities AS u ON u.UtilityID = p.UtilityID
                    """)

    rows = cursor.fetchall()

    pricing_plans = []
    for row in rows:
        pricing_plans.append(row.pricingPlan)

    return pricing_plans


def get_promo_code():

    logger.info('product_repository.get_promo_code(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('SELECT promoCode FROM promotions')

    rows = cursor.fetchall()

    promo_codes = []
    for row in rows:
        promo_codes.append(row.promoCode)

    return promo_codes


def get_utility_brands():

    logger.info('product_repository.get_utility_brands(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("""
                        SELECT
                            u.UtilityCode,
                            lower(u.UtilityAbbrev) as UtilityAbbrev,
                            lower(u.State) as State,
                            lower(u.Commodity) as Commodity,
                            b.BrandSlug
                        FROM vw_Utilities AS u
                        INNER JOIN epdata_brandUtility AS bu ON bu.UtilityID = u.UtilityID
                        INNER JOIN epdata_brand AS b ON bu.BrandID = b.BrandID
                    """)

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    utility_brands = []
    for row in rows:
        utility_brands.append(dict(zip(columns, row)))

    return utility_brands


def get_vas_code():

    logger.info('product_repository.get_vas_code(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('SELECT valueAddedServiceCode FROM valueAddedServices')

    rows = cursor.fetchall()

    vas_codes = []
    for row in rows:
        vas_codes.append(row.valueAddedServiceCode)

    return vas_codes





