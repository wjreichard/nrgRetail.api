from service import products_validate_multiple_fields as validator
import unittest


class TestProductsValidateMultipleFields(unittest.TestCase):


    def test_validate_valid(self):
        assert (True is False)


    def test_check_bundle_description_bundle_name_bundle_slug_combination(self):
        assert (True is False)


    def test_check_brand_commodity_state_utility_abbreviation_utility_code_combination(self):
        assert (True is False)


    def test_check_ecf_terms_of_service_type_non_variable_combination(self):
        assert (True is False)


    def test_check_ecf_terms_of_service_type_variable_combination(self):
        assert (True is False)

    def test_check_green_percentage_vas_code_pair_combination(self):
        assert (True is False)


    def test_check_green_percentage_vas_code_match_combination(self):
        assert (True is False)


    def test_check_ongoing_frequency_ongoing_value_combination(self):
        assert (True is False)


    def test_check_partner_code_promo_code_combination(self):
        assert (True is False)


    def test_check_merchandise_merchandise_slug_merchandise_vesting_combination(self):
        assert (True is False)


    def test_check_signup_bonus_signup_vesting_combination(self):
        assert (True is False)


    def test_is_brand_commodity_state_utility_abbreviation_utility_code_valid(self):
        brand = 'nrg_residential'
        commodity = 'electric'
        state = 'pa'
        utility_abbreviation = 'ppl'
        utility_code = '15'

        result = validator.is_brand_commodity_state_utility_abbreviation_utility_code_valid(brand,
                                                                                            commodity,
                                                                                            state,
                                                                                            utility_abbreviation,
                                                                                            utility_code)

        self.assertEqual(result, True,
                         'Expected Brand, Commodity, State, UtilityAbbrev, UtilityCode combination not found.')


    def test_is_bundle_name_bundle_description_bundle_slug_valid(self):
        self.assertEqual(False, True, '')


    def test_is_ecf_terms_of_service_type_non_variable_valid(self):
        self.assertEqual(False, True, '')


    def test_is_ecf_terms_of_service_type_variable_valid(self):
        self.assertEqual(False, True, '')


    def is_green_percentage_vas_code_match_valid(self):
        self.assertEqual(False, True, '')


    def is_green_percentage_vas_code_pair_valid(self):
        self.assertEqual(False, True, '')


    def test_is_merchandise_merchandise_slug_merchandise_vesting_all_empty_valid(self):
        merchandise = ''
        merchandise_slug = ''
        merchandise_vesting = ''

        result = validator.is_merchandise_merchandise_slug_merchandise_vesting_valid(merchandise,
                                                                                     merchandise_slug,
                                                                                     merchandise_vesting)

        self.assertEqual(result, True, 'Expected merchandise-merchandise_slug-merchandise_vesting is invalid.')


    def test_is_merchandise_merchandise_slug_merchandise_vesting_all_populated_valid(self):
        merchandise = 'boo'
        merchandise_slug = 'foo'
        merchandise_vesting = 'goo'

        result = validator.is_merchandise_merchandise_slug_merchandise_vesting_valid(merchandise,
                                                                                     merchandise_slug,
                                                                                     merchandise_vesting)

        self.assertEqual(result, True, 'Expected valid merchandise-merchandise_slug-merchandise_vesting is invalid.')

    def test_is_merchandise_merchandise_slug_merchandise_vesting_invalid(self):
        merchandise = 'boo'
        merchandise_slug = ''
        merchandise_vesting = 'goo'

        result = validator.is_merchandise_merchandise_slug_merchandise_vesting_valid(merchandise,
                                                                                     merchandise_slug,
                                                                                     merchandise_vesting)

        self.assertEqual(result, False, 'Expected invalid merchandise-merchandise_slug-merchandise_vesting is valid.')


    def test_is_ongoing_frequency_ongoing_value_valid(self):
        self.assertEqual(False, True, '')


    def test_is_partner_code_promo_code_valid(self):
        partner_code = 'nrr'
        promo_code = '500'

        result = validator.is_partner_code_promo_code_valid(partner_code, promo_code)

        self.assertEqual(result, True,
                         'Expected PartnerCode, PromoCode combination not found.')


    def test_is_signup_bonus_signup_vesting_all_empty_valid(self):
        signup_bonus = ''
        signup_vesting = ''

        result = validator.is_signup_bonus_signup_vesting_valid(signup_bonus, signup_vesting)

        self.assertEqual(result, True, 'Expected signup_bonus-signup_vesting is invalid.')


    def test_is_signup_bonus_signup_vesting_all_populated_valid(self):
        signup_bonus = '$25'
        signup_vesting = '3 Months'

        result = validator.is_signup_bonus_signup_vesting_valid(signup_bonus, signup_vesting)

        self.assertEqual(result, True, 'Expected signup_bonus-signup_vesting is invalid.')


if __name__ == '__main__':
    unittest.main()