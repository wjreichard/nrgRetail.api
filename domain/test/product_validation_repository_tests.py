import unittest
from domain import product_validation_repository as repo


class TestProductRepository(unittest.TestCase):
    def test_does_active_offer_charge_id_exist(self):
        offer_charge_id = 1

        self.assertEqual(repo.does_active_offer_charge_id_exist(offer_charge_id), True,
                         'Expected Offer Charge ID not found.')

    def test_does_valid_offer_code_exist(self):
        offer_code = '6A6BCE'

        self.assertEqual(repo.does_valid_offer_code_exist(offer_code), True, 'Expected Offer Code not found.')

    def test_get_brand_commodity_state_utility_abbreviation_utility_code(self):
        expected = {
            'BrandSlug': 'nrg_residential',
            'State': 'nj',
            'UtilityAbbrev': 'pseg',
            'Commodity': 'electric',
            'UtilityCode': '29'
        }

        result = repo.get_brand_commodity_state_utility_abbreviation_utility_code()

        self.assertEqual(expected in result, True,
                         'Expected brand, commodity, state, utility_abbreviation, utility_code not found.')

    def test_get_brand_slugs(self):
        brand_slug = 'nrg_residential'
        brand_slugs = repo.get_brand_slugs()

        self.assertEqual(brand_slug in brand_slugs, True, 'Expected Brand Slug not found.')

    def test_get_channels(self):
        channel = 'web'
        channels = repo.get_channels()

        self.assertEqual(channel in channels, True, 'Expected Channel not found.')

    def test_get_partner_codes(self):
        partner_code = 'USA'
        partner_codes = repo.get_partner_codes()

        self.assertEqual(partner_code in partner_codes, True, 'Expected Partner Code not found.')


    def test_get_get_partner_promotion_codes(self):
        expected = {
            'PartnerCode': 'nrr',
            'PromoCode': '500'
        }

        result = repo.get_partner_promotion_codes()

        self.assertEqual(expected in result, True,
                         'Expected PartnerCode / PromoCode not found.')


    def test_get_premise_types(self):
        premise_type = 'Commercial'
        premise_types = repo.get_premise_types()

        self.assertEqual(premise_type in premise_types, True, 'Expected Premise Type not found.')


    def test_get_promo_code(self):
        promo_code = '007'
        promo_codes = repo.get_promo_code()

        self.assertEqual(promo_code in promo_codes, True, 'Expected Premise Type not found.')

    def test_get_vas_code(self):
        vas_code = '007'
        vas_codes = repo.get_vas_code()

        self.assertEqual(vas_code in vas_codes, True, 'Expected VAS Code not found.')


    def test_get_vas_code_percentages(self):
        expected = {'GreenPercentage': '25%', 'VAS_Code': '003'}
        vas_code_percentages = repo.get_vas_code_percentages()

        self.assertEqual(expected in vas_code_percentages, True, 'Expected VASCodePercentage not found.')




if __name__ == '__main__':
    unittest.main()






