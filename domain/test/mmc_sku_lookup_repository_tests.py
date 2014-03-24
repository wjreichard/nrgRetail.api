import unittest
from domain import mmc_sku_lookup_repository as sku_repo
from service import utility

some_sku_that_exists = '1263B3B9-37ED'


class TestMmcSkuLookupRepository(unittest.TestCase):
    def test_activate_products(self):
        self.assertEqual(False, True)

    def test_deactivate_products(self):
        rows_deactivated = sku_repo.deactivate_products(sku_repo.get_active_product_catalog_id(), 'rike', False)
        self.assertEqual(rows_deactivated > 0, True)

    def test_get_active_product_catalog_id(self):
        result = sku_repo.get_active_product_catalog_id()
        self.assertEqual(result > 0, True)

    def test_get_active_products(self):
        result = sku_repo.get_active_products()
        self.assertEqual(len(result[0]["SKU"]), 13)

    def test_get_by_sku_with_valid_sku(self):
        mmc_sku_lookup = sku_repo.get_product_by_sku(some_sku_that_exists)
        self.assertEqual(mmc_sku_lookup["SKU"], some_sku_that_exists)

    def test_is_sku_not_in_use_where_sku_exists(self):
        result = sku_repo.is_sku_in_use(some_sku_that_exists)
        self.assertEqual(result, True)

    def test_is_sku_not_in_use_where_sku_does_not_exists(self):
        result = sku_repo.is_sku_in_use("foo")
        self.assertEqual(result, False)


    def test_insert_product(self):
        sku = utility.sku_generator()
        product = {
            'Active': True,
            'BrandSlug': 'nrg_residential',
            'BundleDescription': 'Basic Web Variable Plan',
            'BundleName': 'Essentials Plan (Variable)',
            'BundleSlug': 'variable',
            'Channel': 'web',
            'ComcastPTC_Discount': 0,
            'Commodity': 'electric',
            'DefaultBundle': False,
            'ECF': 0.00,
            'EffectiveDate': '3/1/2014',
            'GreenPercentage': '0',
            'LockType': '',
            'Merchandise': '',
            'MerchandiseSlug': '',
            'MerchandiseVesting': '',
            'OngoingFrequency': '3 Months',
            'OngoingValue': '1%',
            'PartnerCode': 'nrr',
            'PricingTerm': 3,
            'PremiseType': 'residential',
            'PromoCode': '500',
            'Rate': 0.084,
            'State': 'pa',
            'SignupBonus': '$25',
            'SignupVesting': '3 Months',
            'SKU': '{}'.format(sku),
            'Sunday2cents': 'Y',
            'TermsOfServiceType': '',
            'UtilityAbbrev': 'ppl',
            'UtilityCode': '15',
            'VAS_Code': '006'
        }

        result = sku_repo.insert_product(product, 1, 'rike', False)
        self.assertEqual(result > 0, True)


    def test_sku_generator(self):

        result = sku_repo.sku_generator()
        self.assertEqual(len(result), 13)


if __name__ == '__main__':
    unittest.main()