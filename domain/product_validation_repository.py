import logging, pyodbc
from config import config
from domain import repository


connection_string = config.enrollment_connection_string
logger = logging.getLogger('api')


def get_brand_commodity_state_utility_abbreviation_utility_code():
    logger.debug('product_validation_repository.get_brand_commodity_state_utility_abbreviation_utility_code(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute("""
                        SELECT
                                LOWER(b.BrandSlug) AS BrandSlug,
                                LOWER(u.Commodity) AS Commodity,
                                LOWER(u.State) AS State,
                                LOWER(u.UtilityAbbrev) as UtilityAbbrev,
                                u.UtilityCode
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


def get_brand_slugs():
    logger.debug('product_validation_repository.get_brand_slugs(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT BrandSlug FROM epdata_brand WHERE brandSlug = \'nrg_residential\'')

        rows = cursor.fetchall()

        brand_slugs = []
        for row in rows:
            brand_slugs.append(row.BrandSlug)

        return brand_slugs


def get_channels():
    logger.debug('product_validation_repository.get_channels(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT name FROM apiChannels')

        rows = cursor.fetchall()

        channels = []
        for row in rows:
            channels.append(row.name.lower().replace(' ', '_'))

        return channels


def get_partner_codes():
    logger.debug('product_validation_repository.get_partner_codes(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT partnerCode FROM partners')

        rows = cursor.fetchall()

        product_codes = []
        for row in rows:
            product_codes.append(row.partnerCode)

        return product_codes


def get_partner_promotion_codes():
    logger.debug('product_validation_repository.get_partner_codes(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute("""
                            SELECT
                                LOWER(PartnerCode) AS PartnerCode,
                                LOWER(PromoCode) AS PromoCode
                            FROM PartnerPromotions AS pp
                                INNER JOIN Partners on pp.PartnerID = Partners.PartnerID
                                INNER JOIN Promotions on pp.PromotionID = Promotions.PromotionID
        """)

        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        partner_promotions = []
        for row in rows:
            partner_promotions.append(dict(zip(columns, row)))

        return partner_promotions


def get_premise_types():
    logger.debug('product_validation_repository.get_premise_types(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT premiseType FROM premiseType')

        rows = cursor.fetchall()

        premise_types = []
        for row in rows:
            premise_types.append(row.premiseType)

        return premise_types


def get_promo_code():
    logger.debug('product_validation_repository.get_promo_code(): start.')

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('SELECT promoCode FROM promotions')

    rows = cursor.fetchall()

    promo_codes = []
    for row in rows:
        promo_codes.append(row.promoCode)

    return promo_codes


def get_vas_code():
    logger.debug('product_validation_repository.get_vas_code(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT valueAddedServiceCode FROM valueAddedServices')

        rows = cursor.fetchall()

        vas_codes = []
        for row in rows:
            vas_codes.append(row.valueAddedServiceCode)

        return vas_codes


def get_vas_code_percentages():
    logger.debug('product_validation_repository.get_vas_code(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute("SELECT valueAddedServiceCode AS VAS_Code, "
                       "CONVERT(VARCHAR, CAST(ConsumptionMultiplier * 100 AS INT)) + '%' AS GreenPercentage "
                       "FROM ValueAddedServices")

        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        vas_code_percentages = []
        for row in rows:
            vas_code_percentages.append(dict(zip(columns, row)))

        return vas_code_percentages


