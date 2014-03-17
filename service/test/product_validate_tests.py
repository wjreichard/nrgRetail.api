from service import product_validate
import unittest


class TestValidateProduct(unittest.TestCase):

# BEGIN Column validations
    def test_validate_brand_slug(self):
        schema = {'BrandSlug': {'is_valid_brand_slug': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        brand_slug = {'BrandSlug': 'nrg_residential'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(brand_slug),True ,'A valid brand_slug is failing validation')

    def test_brand_slug_does_not_exist(self):
        schema = {'BrandSlug': {'is_valid_brand_slug': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        brand_slug = {'BrandSlug': 'foo'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(brand_slug), False, 'An invalid brand_slug is passing validation')

    def test_valid_channel(self):
        schema = {'Channel': {'is_valid_channel': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        channel_one = {'Channel': 'inbound_telemarketing'}
        channel_two = {'Channel': 'web'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(channel_one), True, 'A valid channel is failing validation')
        self.assertEqual(validator.validate(channel_two), True, 'A valid channel is failing validation')

    def test_invalid_channel(self):
        schema = {'Channel': {'is_valid_channel': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        channel_one = {'Channel': 'foo'}
        channel_two = {'Channel': 'AQ'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(channel_one), False, 'An invalid channel is passing validation')
        self.assertEqual(validator.validate(channel_two), False, 'An invalid channel is passing validation')

    def test_valid_signupBonus(self):
        schema = {'signupBonus': {'is_valid_signupBonus': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        signupBonus = {'signupBonus': '$50'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(signupBonus), True, 'A valid signupBonus is failing validation')

    def test_invalid_signupBonus(self):
        schema = {'signupBonus': {'is_valid_signupBonus': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        signupBonus = {'signupBonus': 'foo'}
        signupBonus2 = {'signupBonus': '$ 50'}
        signupBonus3 = {'signupBonus': 'words $50'}
        signupBonus4 = {'signupBonus': 'failure$50'}
        signupBonus5 = {'signupBonus': '$50.00'}
        signupBonus6 = {'signupBonus': '$50 words'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(signupBonus), False, 'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signupBonus2), False, 'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signupBonus3), False, 'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signupBonus4), False, 'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signupBonus5), False, 'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signupBonus6), False, 'An invalid signupBonus is passing validation')

    def test_valid_premiseType(self):
        schema = {'premiseType': {'is_valid_premiseType': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        premiseType = {'premiseType': 'residential'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(premiseType), True, 'A valid premiseType is failing validation')

    def test_invalid_premiseType(self):
        schema = {'premiseType': {'is_valid_premiseType': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        premiseType = {'premiseType': 'foo'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(premiseType), False, 'An invalid premiseType is passing validation')

    def test_valid_partnerCode(self):
        schema = {'partnerCode': {'is_valid_partnerCode': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        partnerCode = {'partnerCode': 'EGR'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(partnerCode), True, 'A valid partnerCode is failing validation')

    def test_invalid_partnerCode(self):
        schema = {'partnerCode': {'is_valid_partnerCode': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        partnerCode = {'partnerCode': 'foo'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(partnerCode), False, 'An invalid partnerCode is passing validation')

    def test_valid_promoCode(self):
        schema = {'promoCode': {'is_valid_promoCode': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        promoCode = {'promoCode': '700'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(promoCode), True, 'A valid promoCode is failing validation')

    def test_invalid_promoCode(self):
        schema = {'promoCode': {'is_valid_promoCode': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        promoCode = {'promoCode': 'foo'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(promoCode), False, 'An invalid promoCode is passing validation')

    def test_valid_pricingTerm(self):
        schema = {'pricingTerm': {'is_valid_pricingTerm': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        pricingTerm = {'pricingTerm': '6'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(pricingTerm), True, 'A valid pricingTerm is failing validation')

    def test_invalid_pricingTerm(self):
        schema = {'pricingTerm': {'is_valid_pricingTerm': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        pricingTerm = {'pricingTerm': 'foo'}
        pricingTerm2 = {'pricingTerm': '2.5'}
        pricingTerm3 = {'pricingTerm': 'foo 6'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(pricingTerm), False, 'An invalid pricingTerm is passing validation')
        self.assertEqual(validator.validate(pricingTerm2), False, 'An invalid pricingTerm is passing validation')
        self.assertEqual(validator.validate(pricingTerm3), False, 'An invalid pricingTerm is passing validation')

    def test_valid_sunday2cents(self):
        schema = {'sunday2cents': {'is_valid_sunday2cents': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        sunday2cents = {'sunday2cents': 'Y'}
        sunday2cents2 = {'sunday2cents': 'N'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(sunday2cents), True, 'A valid sunday2cents is failing validation')
        self.assertEqual(validator.validate(sunday2cents2), True, 'A valid sunday2cents is failing validation')

    def test_invalid_sunday2cents(self):
        schema = {'sunday2cents': {'is_valid_sunday2cents': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        sunday2cents = {'sunday2cents': 'foo'}
        sunday2cents2 = {'sunday2cents': 'fooY'}
        sunday2cents3 = {'sunday2cents': ' Y'}
        sunday2cents4 = {'sunday2cents': 'Y '}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(sunday2cents), False, 'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday2cents2), False, 'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday2cents3), False, 'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday2cents4), False, 'An invalid sunday2cents is passing validation')

    def test_valid_vasCode(self):
        schema = {'vasCode': {'is_valid_vasCode': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        vasCode = {'vasCode': '006'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(vasCode), True, 'A valid vasCode is failing validation')

    def test_invalid_vasCode(self):
        schema = {'vasCode': {'is_valid_vasCode': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        vasCode = {'vasCode': 'foo'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(vasCode), False, 'An invalid vasCode is passing validation')

    def test_valid_rateShownToCustomer(self):
        schema = {'rateShownToCustomer': {'is_valid_rateShownToCustomer': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        rateShownToCustomer = {'rateShownToCustomer': '0.05'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(rateShownToCustomer), True, 'A valid rateShownToCustomer is failing validation')

    def test_invalid_rateShownToCustomer(self):
        schema = {'rateShownToCustomer': {'is_valid_rateShownToCustomer': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        rateShownToCustomer = {'rateShownToCustomer': 'foo'}
        rateShownToCustomer2 = {'rateShownToCustomer': '100'}
        #rateShownToCustomer3 = {'rateShownToCustomer': '100.00'}
        rateShownToCustomer4 = {'rateShownToCustomer': '0.039458'}
        rateShownToCustomer5 = {'rateShownToCustomer': ''}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(rateShownToCustomer), False, 'An invalid rateShownToCustomer is passing validation')
        self.assertEqual(validator.validate(rateShownToCustomer2), False, 'An invalid rateShownToCustomer is passing validation')
       #self.assertEqual(validator.validate(rateShownToCustomer3), False, 'An invalid rateShownToCustomer is passing validation')
        self.assertEqual(validator.validate(rateShownToCustomer4), False, 'An invalid rateShownToCustomer is passing validation')
        self.assertEqual(validator.validate(rateShownToCustomer5), False, 'An invalid rateShownToCustomer is passing validation')

    def test_valid_ongoingValue(self):
        schema = {'ongoingValue': {'is_valid_ongoingValue': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        ongoingValue = {'ongoingValue': '1%'}
        ongoingValue2 = {'ongoingValue': ''}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ongoingValue), True, 'A valid ongoingValue is failing validation')
        self.assertEqual(validator.validate(ongoingValue2), True, 'A valid ongoingValue is failing validation')

    def test_invalid_ongoingValue(self):
        schema = {'ongoingValue': {'is_valid_ongoingValue': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        ongoingValue = {'ongoingValue': 'foo'}
        ongoingValue2 = {'ongoingValue': 'f%'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ongoingValue), False, 'An invalid ongoingValue is passing validation')
        self.assertEqual(validator.validate(ongoingValue2), False, 'An invalid ongoingValue is passing validation')

    def test_valid_ECF(self):
        schema = {'ECF': {'is_valid_ECF': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        ECF = {'ECF': '50.00'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ECF), True, 'A valid ECF is failing validation')

    def test_invalid_ECF(self):
        schema = {'ECF': {'is_valid_ECF': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        ECF = {'ECF': 'foo'}
        ECF2 = {'ECF': '50'}
        ECF3 = {'ECF': '$50'}
        ECF4 = {'ECF': '$50.00'}
        ECF5 = {'ECF': '50.001'}
        ECF6 = {'ECF': '5.00.00'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ECF), False, 'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ECF2), False, 'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ECF3), False, 'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ECF4), False, 'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ECF5), False, 'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ECF6), False, 'An invalid ECF is passing validation')

    def test_valid_merchandiseVesting(self):
        schema = {'merchandiseVesting': {'is_valid_merchandiseVesting': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        merchandiseVesting = {'merchandiseVesting': '20 days'}
        merchandiseVesting2 = {'merchandiseVesting': '12 months'}
        merchandiseVesting3 = {'merchandiseVesting': '20 Days'}
        merchandiseVesting4 = {'merchandiseVesting': '12 Months'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(merchandiseVesting), True, 'A valid merchandiseVesting is failing validation')
        self.assertEqual(validator.validate(merchandiseVesting2), True, 'A valid merchandiseVesting is failing validation')
        self.assertEqual(validator.validate(merchandiseVesting3), True, 'A valid merchandiseVesting is failing validation')
        self.assertEqual(validator.validate(merchandiseVesting4), True, 'A valid merchandiseVesting is failing validation')

    def test_invalid_merchandiseVesting(self):
        schema = {'merchandiseVesting': {'is_valid_merchandiseVesting': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        merchandiseVesting = {'merchandiseVesting': 'foo'}
        merchandiseVesting2= {'merchandiseVesting': '1 year'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(merchandiseVesting), False, 'An invalid merchandiseVesting is passing validation')
        self.assertEqual(validator.validate(merchandiseVesting2), False, 'An invalid merchandiseVesting is passing validation')

    def test_valid_signupVesting(self):
        schema = {'signupVesting': {'is_valid_signupVesting': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        signupVesting = {'signupVesting': '20 days'}
        signupVesting2 = {'signupVesting': '12 months'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(signupVesting), True, 'A valid signupVesting is failing validation')
        self.assertEqual(validator.validate(signupVesting2), True, 'A valid signupVesting is failing validation')

    def test_invalid_signupVesting(self):
        schema = {'signupVesting': {'is_valid_signupVesting': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        signupVesting = {'signupVesting': 'foo'}
        signupVesting2 = {'signupVesting': '1 year'}
        signupVesting3 = {'signupVesting': '2.5 months'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(signupVesting), False, 'An invalid signupVesting is passing validation')
        self.assertEqual(validator.validate(signupVesting2), False, 'An invalid signupVesting is passing validation')
        self.assertEqual(validator.validate(signupVesting3), False, 'An invalid signupVesting is passing validation')

    def test_valid_ongoingFrequency(self):
        schema = {'ongoingFrequency': {'is_valid_ongoingFrequency': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        ongoingFrequency = {'ongoingFrequency': '20 days'}
        ongoingFrequency2 = {'ongoingFrequency': '24 months'}
        ongoingFrequency3 = {'ongoingFrequency': '20 Days'}
        ongoingFrequency4 = {'ongoingFrequency': '24 Months'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ongoingFrequency), True, 'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoingFrequency2), True, 'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoingFrequency3), True, 'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoingFrequency4), True, 'A valid ongoingFrequency is failing validation')

    def test_invalid_ongoingFrequency(self):
        schema = {'ongoingFrequency': {'is_valid_ongoingFrequency': True, 'type': 'string'}, 'Extra': {'type': 'string'}}
        ongoingFrequency = {'ongoingFrequency': 'foo'}
        ongoingFrequency2 = {'ongoingFrequency': '1 year'}
        ongoingFrequency3 = {'ongoingFrequency': '2.5 months'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ongoingFrequency), False, 'An invalid ongoingFrequency is passing validation')
        self.assertEqual(validator.validate(ongoingFrequency2), False, 'An invalid ongoingFrequency is passing validation')
        self.assertEqual(validator.validate(ongoingFrequency3), False, 'An invalid ongoingFrequency is passing validation')

    def test_valid_utilityBrandState(self):
        schema= {'product': {'type': 'dict', "is_valid_utilityBrandState":"True", 'schema':  { "BrandSlug": {"type": "string", "required":"True"} ,
                                                           "Channel": {"type": "string", "required":"True"},
                                                           "BundleName": { "type": "string"},
                                                           "BundleDescription": { "type": "string"},
                                                           "Commodity": { "type": "string"},
                                                           "ECF": {"type": "string"},
                                                           "VAS_Code": {"type": "string"},
                                                           "LockType": { "type": "string"},
                                                           "MerchandiseSlug": { "type": "string"},
                                                           "MerchandiseVesting": { "type": "string"},
                                                           "OngoingFrequency": { "type": "string"},
                                                           "OngoingValue": { "type": "string"},
                                                           "PartnerCode": { "type": "string"},
                                                           "PremiseType": { "type": "string"},
                                                           "PricingTerm": { "type": "string", "required":"True"},
                                                           "PromoCode": { "type": "string"},
                                                           "Rate": { "type": "string", "required":"True"},
                                                           "SignupBonus": { "type": "string"},
                                                           "SignupVesting": {"type": "string"},
                                                           "StateAbbrev": { "type": "string"},
                                                           "UtilityCode": { "type": "string"},
                                                           "TermsOfServiceType": { "type": "string"},
                                                           "Sunday2cents": { "type": "string"} }}}

        product = {"product": {"BrandSlug": "nrg_residential", "Channel": "IB", "BundleName":"" ,
                               "BundleDescription":"", "Commodity":"electric", "ECF":"0.00",
                               "VAS_Code":"006", "LockType":"","MerchandiseSlug":"", "MerchandiseVesting":"",
                               "OngoingFrequency":"", "OngoingValue":"", "PartnerCode":"NRR",
                               "PremiseType":"residential", "PricingTerm":"6", "PromoCode":"700",
                               "Rate":"0.12", "SignupBonus":"", "SignupVesting":"",
                               "StateAbbrev":"pa", "UtilityCode":"16", "TermsOfServiceType":"", "Sunday2cents":"Y"}}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(product), True, 'A valid utilityBrandState is failing validation')

    def test_invalid_utilityBrandState(self):
        schema= {'product': {'type': 'dict', "is_valid_utilityBrandState":"True", 'schema':  { "BrandSlug": {"type": "string", "required":"True"} ,
                                                           "Channel": {"type": "string", "required":"True"},
                                                           "BundleName": { "type": "string"},
                                                           "BundleDescription": { "type": "string"},
                                                           "Commodity": { "type": "string"},
                                                           "ECF": {"type": "string"},
                                                           "VAS_Code": {"type": "string"},
                                                           "LockType": { "type": "string"},
                                                           "MerchandiseSlug": { "type": "string"},
                                                           "MerchandiseVesting": { "type": "string"},
                                                           "OngoingFrequency": { "type": "string"},
                                                           "OngoingValue": { "type": "string"},
                                                           "PartnerCode": { "type": "string"},
                                                           "PremiseType": { "type": "string"},
                                                           "PricingTerm": { "type": "string", "required":"True"},
                                                           "PromoCode": { "type": "string"},
                                                           "Rate": { "type": "string", "required":"True"},
                                                           "SignupBonus": { "type": "string"},
                                                           "SignupVesting": {"type": "string"},
                                                           "StateAbbrev": { "type": "string"},
                                                           "UtilityCode": { "type": "string"},
                                                           "TermsOfServiceType": { "type": "string"},
                                                           "Sunday2cents": { "type": "string"} }}}

        product = {"product": {"BrandSlug": "nrg_residential", "Channel": "IB", "BundleName":"" ,
                               "BundleDescription":"", "Commodity":"electric", "ECF":"0.00",
                               "VAS_Code":"006", "LockType":"","MerchandiseSlug":"", "MerchandiseVesting":"",
                               "OngoingFrequency":"", "OngoingValue":"", "PartnerCode":"NRR",
                               "PremiseType":"residential", "PricingTerm":"6", "PromoCode":"700",
                               "Rate":"0.12", "SignupBonus":"", "SignupVesting":"",
                               "StateAbbrev":"md", "UtilityCode":"16", "TermsOfServiceType":"", "Sunday2cents":"Y"}}

        product2 = {"product": {"BrandSlug": "energy_rewards", "Channel": "IB", "BundleName":"" ,
                               "BundleDescription":"", "Commodity":"electric", "ECF":"0.00",
                               "VAS_Code":"006", "LockType":"","MerchandiseSlug":"", "MerchandiseVesting":"",
                               "OngoingFrequency":"", "OngoingValue":"", "PartnerCode":"NRR",
                               "PremiseType":"residential", "PricingTerm":"6", "PromoCode":"700",
                               "Rate":"0.12", "SignupBonus":"", "SignupVesting":"",
                               "StateAbbrev":"md", "UtilityCode":"35", "TermsOfServiceType":"", "Sunday2cents":"Y"}}

        product3 = {"product": {"BrandSlug": "nrg_residential", "Channel": "IB", "BundleName":"" ,
                               "BundleDescription":"", "Commodity":"gas", "ECF":"0.00",
                               "VAS_Code":"006", "LockType":"","MerchandiseSlug":"", "MerchandiseVesting":"",
                               "OngoingFrequency":"", "OngoingValue":"", "PartnerCode":"NRR",
                               "PremiseType":"residential", "PricingTerm":"6", "PromoCode":"700",
                               "Rate":"0.12", "SignupBonus":"", "SignupVesting":"",
                               "StateAbbrev":"md", "UtilityCode":"35", "TermsOfServiceType":"", "Sunday2cents":"Y"}}
        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(product), False, 'An invalid utilityBrandState is passing validation')
        self.assertEqual(validator.validate(product2), False, 'An invalid utilityBrandState is passing validation')
        self.assertEqual(validator.validate(product3), False, 'An invalid utilityBrandState is passing validation')


if __name__ == '__main__':
    unittest.main()

