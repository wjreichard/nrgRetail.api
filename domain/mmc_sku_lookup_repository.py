import logging
from domain import repository
from config import config


connection_string = config.enrollment_connection_string
logger = logging.getLogger('api')


def deactivate_products(product_catalog_id, user, commit):

    logger.info('mmc_sku_lookup_repository.deactivate_products(): start.')

    with repository.open_db_connection(connection_string, commit) as cursor:
        cursor.execute('UPDATE dbo.MMC_Sku_Lookup SET Active = 0, UpdateUser = ? WHERE ProductCatalogID = ?',
                        user, product_catalog_id)
        return cursor.rowcount

def get_active_product_catalog_id():

    logger.info('mmc_sku_lookup_repository.get_active_product_catalog_id(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT DISTINCT(ProductCatalogID) FROM dbo.MMC_Sku_Lookup WHERE Active = 1')
        rows = cursor.fetchall()

        if len(rows) is not 1:
            raise Exception(
                'mmc_sku_lookup_repository.get_active_product_catalog_id(): more than one product catalog is active.')

        return rows[0][0]


def get_active_products():

    logger.info('mmc_sku_lookup_repository.get_active_products(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute("""
                            SELECT top 10 *
                            FROM mmc_sku_lookup WHERE active = 1
                       """)

        return [dict(zip([column[0] for column in cursor.description], row))
             for row in cursor.fetchall()]


def get_product_by_sku(sku):

    logger.info('mmc_sku_lookup_repository.get_product_by_sku(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT * FROM mmc_sku_lookup WHERE sku = \'{0}\''.format(sku))

        return dict(zip([column[0] for column in cursor.description], cursor.fetchone()))


def insert_product(product, product_catalog_id, user, commit):

    logger.info('mmc_sku_lookup_repository.insert_product(): start.')

    with repository.open_db_connection(connection_string, commit) as cursor:
        cursor.execute("""
                            INSERT INTO [dbo].[MMC_SKU_Lookup]
                                       (
                                            Active,
                                            BrandSlug,
                                            BundleDescription,
                                            BundleName,
                                            BundleSlug,
                                            Channel,
                                            ComcastPTC_Discount,
                                            Commodity,
                                            DefaultBundle,
                                            ECF,
                                            EffectiveDate,
                                            GreenPercentage,
                                            InsertUser,
                                            LockType,
                                            Merchandise,
                                            MerchandiseSlug,
                                            MerchandiseVesting,
                                            OngoingFrequency,
                                            OngoingValue,
                                            PartnerCode,
                                            PremiseType,
                                            PricingTerm,
                                            ProductCatalogID,
                                            PromoCode,
                                            Rate,
                                            SKU,
                                            SignupBonus,
                                            SignupVesting,
                                            State,
                                            Sunday2cents,
                                            TermsOfServiceType,
                                            UtilityAbbrev,
                                            UtilityCode,
                                            VAS_Code
                                        )
                                 OUTPUT INSERTED.SKU_ID
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                         ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                         ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                         ?, ?, ?, ?)""",
                                         True,
                                         product["BrandSlug"],
                                         product["BundleDescription"],
                                         product["BundleName"],
                                         product["BundleSlug"],
                                         product["Channel"],
                                         float(product["ComcastPTC_Discount"]),
                                         product["Commodity"],
                                         bool(product["DefaultBundle"]),
                                         float(product["ECF"]),
                                         product["EffectiveDate"],
                                         product["GreenPercentage"],
                                         user,
                                         product["LockType"],
                                         product["Merchandise"],
                                         product["MerchandiseSlug"],
                                         product["MerchandiseVesting"],
                                         product["OngoingFrequency"],
                                         product["OngoingValue"],
                                         product["PartnerCode"],
                                         product["PremiseType"],
                                         int(product["PricingTerm"]),
                                         product_catalog_id,
                                         product["PromoCode"],
                                         float(product["Rate"]),
                                         product["SKU"],
                                         product["SignupBonus"],
                                         product["SignupVesting"],
                                         product["State"],
                                         product["Sunday2cents"],
                                         product["TermsOfServiceType"],
                                         product["UtilityAbbrev"],
                                         product["UtilityCode"],
                                         product["VAS_Code"])
        row = cursor.fetchone()
        return row[0]


def is_sku_in_use(sku):

    logger.info('mmc_sku_lookup_repository.is_sku_in_use(): start.')

    with repository.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT sku FROM mmc_sku_lookup WHERE sku = \'{0}\''.format(sku))
        return cursor.fetchone() is not None