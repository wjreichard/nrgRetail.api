import unittest
from service import products_validate_file as validator


some_product_catalog_id_that_exists = 250


class TestProductsValidateFile(unittest.TestCase):
    def test_validate_valid(self):
        csv = '"BrandSlug", "BundleDescription", "BundleName", "BundleSlug", "Channel", "Commodity", ' \
              '"DefaultBundle", "ECF", "EffectiveDate", "GreenPercentage", "LockType", "Merchandise", ' \
              '"MerchandiseSlug", "MerchandiseVesting", "OngoingFrequency", "OngoingValue", "PartnerCode", ' \
              '"PremiseType", "PricingTerm", "PromoCode", "Rate", "SignupBonus", "SignupVesting", "State", ' \
              '"Sunday2cents", "TermsOfServiceType", "UtilityAbbrev", "UtilityCode", "VAS_Code"'

        self.assertEqual(not validator.validate(csv), True)


    def test_validate_not_comma_delimited_invalid(self):
        csv = 'boo|foo'

        self.assertEqual(not validator.validate(csv), False)


    def test_validate_extra_column_invalid(self):
        csv = '"BrandSlug", "foo", "BundleDescription", "BundleName", "BundleSlug", "Channel", "Commodity", ' \
              '"DefaultBundle", "ECF", "EffectiveDate", "GreenPercentage", "LockType", "Merchandise", ' \
              '"MerchandiseSlug", "MerchandiseVesting", "OngoingFrequency", "OngoingValue", "PartnerCode", ' \
              '"PremiseType", "PricingTerm", "PromoCode", "Rate", "SignupBonus", "SignupVesting", "State", ' \
              '"Sunday2cents", "TermsOfServiceType", "UtilityAbbrev", "UtilityCode", "VAS_Code"'

        self.assertEqual(not validator.validate(csv), False)


    def test_validate_missing_column_invalid(self):
        csv = '"BrandSlug", "BundleName", "BundleSlug", "Channel", "Commodity", ' \
              '"DefaultBundle", "ECF", "EffectiveDate", "GreenPercentage", "LockType", "Merchandise", ' \
              '"MerchandiseSlug", "MerchandiseVesting", "OngoingFrequency", "OngoingValue", "PartnerCode", ' \
              '"PremiseType", "PricingTerm", "PromoCode", "Rate", "SignupBonus", "SignupVesting", "State", ' \
              '"Sunday2cents", "TermsOfServiceType", "UtilityAbbrev", "UtilityCode", "VAS_Code"'

        self.assertEqual(not validator.validate(csv), False)


    def test_validate_extra_and_missing_columns_invalid(self):
        csv = '"BrandSlug", "BOO", "BundleName", "BundleSlug", "Channel", "Commodity", ' \
              '"DefaultBundle", "ECF", "EffectiveDate", "GreenPercentage", "LockType", "Merchandise", ' \
              '"MerchandiseSlug", "MerchandiseVesting", "OngoingFrequency", "OngoingValue", "PartnerCode", ' \
              '"PremiseType", "PricingTerm", "PromoCode", "Rate", "SignupBonus", "SignupVesting", "State", ' \
              '"Sunday2cents", "TermsOfServiceType", "UtilityAbbrev", "UtilityCode", "VAS_Code"'
        print(validator.validate(csv))
        self.assertEqual(len(validator.validate(csv)) == 2, True)


    def test_is_csv_valid(self):
        errors = []
        csv = 'boo,foo'

        self.assertEqual(not validator.is_csv(csv, errors), True)

    def test_is_csv_invalid(self):
        errors = []
        csv = 'boo|foo'

        self.assertEqual(not validator.is_csv(csv, errors), False)


    def test_are_all_columns_expected_valid(self):
        errors = []
        csv = 'BrandSlug, BundleDescription, BundleName, BundleSlug, Channel, Commodity, ' \
              'DefaultBundle, ECF, EffectiveDate, GreenPercentage, LockType, Merchandise, ' \
              'MerchandiseSlug, MerchandiseVesting, OngoingFrequency, OngoingValue, PartnerCode, ' \
              'PremiseType, PricingTerm, PromoCode, Rate, SignupBonus, SignupVesting, State, ' \
              'Sunday2cents, TermsOfServiceType, UtilityAbbrev, UtilityCode, VAS_Code'

        self.assertEqual(not validator.are_all_columns_expected(csv, errors), True)


    def test_are_all_columns_expected_quoted_valid(self):
        errors = []
        csv = '"BrandSlug", "BundleDescription", "BundleName", "BundleSlug", "Channel", "Commodity", ' \
              '"DefaultBundle", "ECF", "EffectiveDate", "GreenPercentage", "LockType", "Merchandise", ' \
              '"MerchandiseSlug", "MerchandiseVesting", "OngoingFrequency", "OngoingValue", "PartnerCode", ' \
              '"PremiseType", "PricingTerm", "PromoCode", "Rate", "SignupBonus", "SignupVesting", "State", ' \
              '"Sunday2cents", "TermsOfServiceType", "UtilityAbbrev", "UtilityCode", "VAS_Code"'

        self.assertEqual(not validator.are_all_columns_expected(csv, errors), True)


    def test_are_all_columns_expected_invalid(self):
        csv_1 = 'boo, foo'

        csv_2 = 'Brand Slug, BundleDescription, BundleName, BundleSlug, Channel, Commodity, ' \
                'DefaultBundle, ECF, EffectiveDate, GreenPercentage, LockType, Merchandise, ' \
                'MerchandiseSlug, MerchandiseVesting, OngoingFrequency, OngoingValue, PartnerCode, ' \
                'PremiseType, PricingTerm, PromoCode, Rate, SignupBonus, SignupVesting, State, ' \
                'Sunday2cents, TermsOfServiceType, UtilityAbbrev, UtilityCode, VAS_Code'

        errors = []
        self.assertEqual(not validator.are_all_columns_expected(csv_1, errors), False)

        errors = []
        self.assertEqual(not validator.are_all_columns_expected(csv_2, errors), False)


    def test_are_all_columns_expected_quoted_invalid(self):
        csv_1 = '"boo", "foo"'

        csv_2 = '"BrandSlug", "BundleDescriptionBOO", "BundleName", "BundleSlug", "Channel", "Commodity", ' \
                '"DefaultBundle", "ECF", "EffectiveDate", "GreenPercentage", "LockType", "Merchandise", ' \
                '"MerchandiseSlug", "MerchandiseVesting", "OngoingFrequency", "OngoingValue", "PartnerCode", ' \
                '"PremiseType", "PricingTerm", "PromoCode", "Rate", "SignupBonus", "SignupVesting", "State", ' \
                '"Sunday2cents", "TermsOfServiceType", "UtilityAbbrev", "UtilityCode", "VAS_Code"'

        errors = []
        self.assertEqual(not validator.are_all_columns_expected(csv_1, errors), False)

        errors = []
        self.assertEqual(not validator.are_all_columns_expected(csv_2, errors), False)


    def test_are_any_columns_missing_valid(self):
        errors = []
        csv = 'BrandSlug, BundleDescription, BundleName, BundleSlug, Channel, Commodity, ' \
              'DefaultBundle, ECF, EffectiveDate, GreenPercentage, LockType, Merchandise, ' \
              'MerchandiseSlug, MerchandiseVesting, OngoingFrequency, OngoingValue, PartnerCode, ' \
              'PremiseType, PricingTerm, PromoCode, Rate, SignupBonus, SignupVesting, State, ' \
              'Sunday2cents, TermsOfServiceType, UtilityAbbrev, UtilityCode, VAS_Code'

        self.assertEqual(not validator.are_any_columns_missing(csv, errors), True)


    def test_any_columns_missing_quoted_valid(self):
        errors = []
        csv = '"BrandSlug", "BundleDescription", "BundleName", "BundleSlug", "Channel", "Commodity", ' \
              '"DefaultBundle", "ECF", "EffectiveDate", "GreenPercentage", "LockType", "Merchandise", ' \
              '"MerchandiseSlug", "MerchandiseVesting", "OngoingFrequency", "OngoingValue", "PartnerCode", ' \
              '"PremiseType", "PricingTerm", "PromoCode", "Rate", "SignupBonus", "SignupVesting", "State", ' \
              '"Sunday2cents", "TermsOfServiceType", "UtilityAbbrev", "UtilityCode", "VAS_Code"'

        self.assertEqual(not validator.are_all_columns_expected(csv, errors), True)


    def test_are_any_columns_missing_invalid(self):
        errors = []

        csv = 'BundleDescription, BundleName, BundleSlug, Channel, Commodity, ' \
              'DefaultBundle, ECF, EffectiveDate, GreenPercentage, LockType, Merchandise, ' \
              'MerchandiseSlug, MerchandiseVesting, OngoingFrequency, OngoingValue, PartnerCode, ' \
              'PremiseType, PricingTerm, PromoCode, Rate, SignupBonus, SignupVesting, State, ' \
              'Sunday2cents, TermsOfServiceType, UtilityAbbrev, UtilityCode, VAS_Code'

        self.assertEqual(not validator.are_any_columns_missing(csv, errors), False)


    def test_are_any_columns_missing_quoted_invalid(self):
        errors = []

        csv = '"BrandSlug", "BundleName", "BundleSlug", "Channel", "Commodity", ' \
              '"DefaultBundle", "ECF", "EffectiveDate", "GreenPercentage", "LockType", "Merchandise", ' \
              '"MerchandiseSlug", "MerchandiseVesting", "OngoingFrequency", "OngoingValue", "PartnerCode", ' \
              '"PremiseType", "PricingTerm", "PromoCode", "Rate", "SignupBonus", "SignupVesting", "State", ' \
              '"Sunday2cents", "TermsOfServiceType", "UtilityAbbrev", "UtilityCode", "VAS_Code"'

        self.assertEqual(not validator.are_any_columns_missing(csv, errors), False)


if __name__ == '__main__':
    unittest.main()