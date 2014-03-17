import unittest
from service import product_catalog
from service.test.product_catalog_test_fixtures import test_cases


class TestValidateProduct(unittest.TestCase):

    def test_create_products_from_bytes(self):

        csv_bytes = '"BrandSlug","Channel"\n"nrg_residential","AQ"\n"nrg_residential","AQ"'.encode('utf-8')
        expected = '"BrandSlug","Channel","Errors"\n"nrg_residential","AQ","{}"\n"nrg_residential","AQ","{}"\n'

        result = product_catalog.create_products_from_bytes(csv_bytes)

        self.assertEqual(expected, result)

    def test_create_products_from_bytes_one_real_product(self):

        csv_bytes = '"z'

        result = product_catalog.create_products_from_bytes(csv_bytes)

        self.assertEqual(expected, result)

    #def test_create_products(self):

        # simpleproducts = [{"BrandSlug": "nrg_residential", "Channel": "IB"}, {"BrandSlug": "nrg_residential", "Channel": "AQ"}]
        # simpleexpected = [{"BrandSlug": "nrg_residential", "Channel": "IB", "Errors": {}}, {"BrandSlug": "nrg_residential", "Channel": "AQ", "Errors": {}}]
        #
        # simpleresult = product_catalog.validate_products_row(simpleproducts)
        #
        # self.assertEqual(simpleresult, simpleexpected)

    #    products = [{"BrandSlug": "nrg_residential", "Channel": "IB", "BundleName":"" , "BundleDescription":"", "Commodity":"electric", "ECF":"0.00", "VAS_Code":"006", "LockType":"","MerchandiseSlug":"", "MerchandiseVesting":"", "OngoingFrequency":"", "OngoingValue":"", "PartnerCode":"NRR", "PremiseType":"residential", "PricingTerm":"6", "PromoCode":"700", "Rate":"0.12", "SignupBonus":"", "SignupVesting":"", "StateAbbrev":"PA", "UtilityCode":"16", "TermsOfServiceType":"", "Sunday2cents":"Y"},
    #                {"BrandSlug": "nrg_residential", "Channel": "AQ", "BundleName":"" , "BundleDescription":"", "Commodity":"electric", "ECF":"100.00", "VAS_Code":"007", "LockType":"","MerchandiseSlug":"", "MerchandiseVesting":"", "OngoingFrequency":"", "OngoingValue":"", "PartnerCode":"NRR", "PremiseType":"residential", "PricingTerm":"12", "PromoCode":"700", "Rate":"0.8450", "SignupBonus":"", "SignupVesting":"", "StateAbbrev":"PA", "UtilityCode":"19", "TermsOfServiceType":"", "Sunday2cents":"N"}]
    #    expected = [{"BrandSlug": "nrg_residential", "Channel": "IB", "BundleName":"" , "BundleDescription":"", "Commodity":"electric", "ECF":"0.00", "VAS_Code":"006", "LockType":"","MerchandiseSlug":"", "MerchandiseVesting":"", "OngoingFrequency":"", "OngoingValue":"", "PartnerCode":"NRR", "PremiseType":"residential", "PricingTerm":"6", "PromoCode":"700", "Rate":"0.12", "SignupBonus":"", "SignupVesting":"", "StateAbbrev":"PA", "UtilityCode":"16", "TermsOfServiceType":"", "Sunday2cents":"Y", "Errors": {}},
    #                 {"BrandSlug": "nrg_residential", "Channel": "AQ", "BundleName":"" , "BundleDescription":"", "Commodity":"electric", "ECF":"100.00", "VAS_Code":"007", "LockType":"","MerchandiseSlug":"", "MerchandiseVesting":"", "OngoingFrequency":"", "OngoingValue":"", "PartnerCode":"NRR", "PremiseType":"residential", "PricingTerm":"12", "PromoCode":"700", "Rate":"0.8450", "SignupBonus":"", "SignupVesting":"", "StateAbbrev":"PA", "UtilityCode":"19", "TermsOfServiceType":"", "Sunday2cents":"N", "Errors": {}}]

    #    result = product_catalog.validate_products_row(products)

    #    self.assertEqual(result, expected)












    #def test_create_products_multiple_valid_products(self):

    #    products = '[{"BrandSlug": "energyplus", "Channel": "web"}, ' \
    #               '{"BrandSlug": "nrg_residential", "Channel": "Retention"}]'
    #    expected = '[{"BrandSlug": "energyplus", "Channel": "web", "Errors": {}}, {"BrandSlug": "nrg_residential", "Channel": "Retention", "Errors": {}}]'
    #    result = product_catalog.create_products_from_json(products)

    #    assert(True is True)

    #def test_do_create_products_from_fixtures(self):

    #    for item in test_cases:
    #        result = product_catalog.validate_individual_product_fields(item['products'])
    #        self.assertEqual(result, item['expected'])

    #def test_do_create_products_from_fi(self):
    #    def mssql():
    #        return "MIcorsql"

    #    def mysql():
    #        return "unix"

    #    repository = mssql

    #    print ("hello %s " % repository())

if __name__ == '__main__':
    unittest.main()

