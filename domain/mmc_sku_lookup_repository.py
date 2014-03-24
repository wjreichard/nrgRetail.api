import logging
import uuid
import sys
from config import config
from domain import repository as repo


connection_string = config.enrollment_connection_string
logger = logging.getLogger('api')


def activate_products(products, product_catalog_id, user, commit):
    logger.debug('mmc_sku_lookup_repository.activate_products(): start.')

    if products:
        deactivate_product_catalog_id = get_active_product_catalog_id()
        logger.info('mmc_sku_lookup_repository.activate_products(): deactivating product catalog id: {0}.'
                    .format(deactivate_product_catalog_id))

        with repo.open_db_connection(connection_string, commit) as cursor:

            cursor.execute("""
                            INSERT INTO dbo.MMC_ProductCatalogEvent (ProductCatalogID, ProductCatalogEventSlug, InsertUser)
                                OUTPUT INSERTED.ProductCatalogEventID
                                  VALUES (?, ?, ?)
                        """, deactivate_product_catalog_id, config.ProductCatalogEventSlugs.Deactivated, user)

            deactivate_products(cursor, deactivate_product_catalog_id, user)

            for p in products:
                p["SKU"] = sku_generator()
                logger.debug('mmc_sku_lookup_repository.activate_products(): insert product SKU: {0}.'.format(p["SKU"]))
                print(insert_product(cursor, p, product_catalog_id, user))
    else:
        raise Exception('mmc_sku_lookup_repository.activate_products(): Activate attempted with no Products.')

    return


def deactivate_products(cursor, product_catalog_id, user):
    logger.debug('mmc_sku_lookup_repository.deactivate_products(): start.')

    cursor.execute('UPDATE dbo.MMC_Sku_Lookup SET Active = 0, UpdateUser = ? WHERE ProductCatalogID = ?',
                   user, product_catalog_id)
    return cursor.rowcount


def get_active_product_catalog_id():
    logger.debug('mmc_sku_lookup_repository.get_active_product_catalog_id(): start.')

    with repo.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT DISTINCT(ProductCatalogID) FROM dbo.MMC_Sku_Lookup WHERE Active = 1')
        rows = cursor.fetchall()

        if len(rows) is not 1:
            raise Exception(
                'mmc_sku_lookup_repository.get_active_product_catalog_id(): more than one product catalog is active.')

        return rows[0][0]


def get_active_products():
    logger.debug('mmc_sku_lookup_repository.get_active_products_as_csv(): start.')

    with repo.open_db_connection(connection_string) as cursor:
        cursor.execute("""
                            SELECT
                                BrandSlug,
                                BundleDescription,
                                BundleName,
                                BundleSlug,
                                Channel,
                                Commodity,
                                DefaultBundle,
                                ROUND(ECF, 2) AS ECF,
                                EffectiveDate,
                                GreenPercentage,
                                LockType,
                                Merchandise,
                                MerchandiseSlug,
                                MerchandiseVesting,
                                OngoingFrequency,
                                OngoingValue,
                                PartnerCode,
                                PremiseType,
                                PricingTerm,
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
                            FROM mmc_sku_lookup WHERE active = 1
                       """)

        return [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]


def get_product_by_sku(sku):
    logger.debug('mmc_sku_lookup_repository.get_product_by_sku(): start.')

    with repo.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT * FROM mmc_sku_lookup WHERE sku = \'{0}\''.format(sku))

        return dict(zip([column[0] for column in cursor.description], cursor.fetchone()))


def insert_product(cursor, product, product_catalog_id, user):
    logger.debug('mmc_sku_lookup_repository.insert_product(): start.')

    cursor.execute("""
                        INSERT INTO [dbo].[MMC_SKU_Lookup]
                                   (
                                        Active,
                                        BrandSlug,
                                        BundleDescription,
                                        BundleName,
                                        BundleSlug,
                                        Channel,
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
                                     ?, ?, ?)""",
                   True,
                   product["BrandSlug"],
                   product["BundleDescription"],
                   product["BundleName"],
                   product["BundleSlug"],
                   product["Channel"],
                   product["Commodity"],
                   bool(product["DefaultBundle"]),
                   product["ECF"],
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
    logger.debug('mmc_sku_lookup_repository.is_sku_in_use(): start.')

    with repo.open_db_connection(connection_string) as cursor:
        cursor.execute('SELECT sku FROM mmc_sku_lookup WHERE sku = \'{0}\''.format(sku))
        return cursor.fetchone() is not None


def sku_generator():

    logger.debug("utility.sku_generator(): start.")

    sku_uid = ''

    for _ in range(100):
        sku_uid = str(uuid.uuid4())[:13]
        if is_sku_in_use(sku_uid) is not True:
            break

    if sku_uid is '':
        raise Exception('mmc_sku_lookup_repository.sku_generator(): After 100 tries, could not find an unused SKU')

    return sku_uid.upper()