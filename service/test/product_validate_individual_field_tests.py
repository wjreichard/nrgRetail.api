from service import product_validate
import unittest


class TestValidateProduct(unittest.TestCase):


    def test_brand_slug_valid(self):

        schema = { 'BrandSlug':
                       { 'is_brand_slug_valid': True, 'type': 'string' }
                 }
        brand_slug = { 'BrandSlug': 'nrg_residential' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(brand_slug),True ,
                         'A valid brand_slug is failing validation')


    def test_brand_slug_does_not_exist(self):

        schema = { 'BrandSlug':
                       { 'is_brand_slug_valid': True, 'type': 'string' }
                 }
        brand_slug = { 'BrandSlug': 'foo' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(brand_slug), False,
                         'An invalid brand_slug is passing validation')


    def test_channel_valid(self):

        schema = { 'Channel':
                       { 'is_channel_valid': True, 'type': 'string' }
                 }
        channel_1 = { 'Channel': 'inbound_telemarketing' }
        channel_2 = { 'Channel': 'web' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(channel_1), True,
                         'A valid channel is failing validation')
        self.assertEqual(validator.validate(channel_2), True,
                         'A valid channel is failing validation')


    def test_channel_invalid(self):

        schema = { 'Channel':
                       { 'is_channel_valid': True, 'type': 'string' }
                 }
        channel_1 = {'Channel': 'foo'}
        channel_2 = {'Channel': 'AQ'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(channel_1), False,
                         'An invalid channel is passing validation')
        self.assertEqual(validator.validate(channel_2), False,
                         'An invalid channel is passing validation')


    def test_default_bundle_valid(self):

        schema = { 'DefaultBundle':
                       { 'is_default_bundle_valid': True, 'type': 'string'}
                 }
        channel_1 = { 'DefaultBundle': 'True' }
        channel_2 = { 'DefaultBundle': 'False' }
        channel_3 = { 'DefaultBundle': '1' }
        channel_4 = { 'DefaultBundle': '0' }
        channel_5 = { 'DefaultBundle': 'tRue' }
        channel_6 = { 'DefaultBundle': 'fAlsE' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(channel_1), True,
                         'A valid default bundle is failing validation')
        self.assertEqual(validator.validate(channel_2), True,
                         'A valid default bundle is failing validation')
        self.assertEqual(validator.validate(channel_3), True,
                         'A valid default bundle is failing validation')
        self.assertEqual(validator.validate(channel_4), True,
                         'A valid default bundle is failing validation')
        self.assertEqual(validator.validate(channel_5), True,
                         'A valid default bundle is failing validation')
        self.assertEqual(validator.validate(channel_6), True,
                         'A valid default bundle is failing validation')


    def test_default_bundle_invalid(self):

        schema = { 'DefaultBundle':
                       { 'is_default_bundle_valid': True, 'type': 'string'}
                 }

        channel_1 = { 'DefaultBundle': '' }
        channel_2 = { 'DefaultBundle': 'foo' }
        channel_3 = { 'DefaultBundle': 1 }
        channel_4 = { 'DefaultBundle': 0 }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(channel_1), False,
                         'An invalid default bundle is passing validation')
        self.assertEqual(validator.validate(channel_2), False,
                         'An invalid default bundle is passing validation')
        self.assertEqual(validator.validate(channel_3), False,
                         'An invalid default bundle is passing validation')
        self.assertEqual(validator.validate(channel_4), False,
                         'An invalid default bundle is passing validation')


    def test_ecf_valid(self):

        schema = { 'ECF':
                       { 'is_ecf_valid': True, 'type': 'string'}
                 }
        ecf = {'ECF': '50.00'}

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ecf), True,
                         'A valid ECF is failing validation')


    def test_ecf_invalid(self):

        schema = { 'ECF':
                       { 'is_ecf_valid': True, 'type': 'string'}
                 }
        ecf_1 = { 'ECF': 'foo' }
        ecf_2 = { 'ECF': '50' }
        ecf_3 = { 'ECF': '$50' }
        ecf_4 = { 'ECF': '$50.00' }
        ecf_5 = { 'ECF': '50.001' }
        ecf_6 = { 'ECF': '5.00.00' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ecf_1), False,
                         'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ecf_2), False,
                         'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ecf_3), False,
                         'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ecf_4), False,
                         'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ecf_5), False,
                         'An invalid ECF is passing validation')
        self.assertEqual(validator.validate(ecf_6), False, 'An invalid ECF is passing validation')


    def test_merchandise_vesting_valid(self):

        schema = { 'merchandiseVesting':
                       { 'is_merchandise_vesting_valid': True, 'type': 'string' }
                 }
        merchandise_vesting_1 = { 'merchandiseVesting': '20 days' }
        merchandise_vesting_2 = { 'merchandiseVesting': '12 months' }
        merchandise_vesting_3 = { 'merchandiseVesting': '20 Days' }
        merchandise_vesting_4 = { 'merchandiseVesting': '12 Months' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(merchandise_vesting_1), True,
                         'A valid merchandiseVesting is failing validation')
        self.assertEqual(validator.validate(merchandise_vesting_2), True,
                         'A valid merchandiseVesting is failing validation')
        self.assertEqual(validator.validate(merchandise_vesting_3), True,
                         'A valid merchandiseVesting is failing validation')
        self.assertEqual(validator.validate(merchandise_vesting_4), True,
                         'A valid merchandiseVesting is failing validation')


    def test_merchandise_vesting_invalid(self):

        schema = {'merchandiseVesting':
                      { 'is_merchandise_vesting_valid': True, 'type': 'string' }
                 }
        merchandise_vesting_1 = { 'merchandiseVesting': 'foo' }
        merchandise_vesting_2= { 'merchandiseVesting': '1 year' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(merchandise_vesting_1), False,
                         'An invalid merchandiseVesting is passing validation')
        self.assertEqual(validator.validate(merchandise_vesting_2), False,
                         'An invalid merchandiseVesting is passing validation')


    def test_offer_charge_id_valid(self):

        schema = { 'OfferChargeID':
                       { 'is_offer_charge_id_valid': True, 'type': 'string' }
                 }
        some_offer_charge_id_that_exists_and_is_active = { 'OfferChargeID': '1' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(some_offer_charge_id_that_exists_and_is_active), True,
                         'A valid OfferChargeID is failing validation')

    def test_offer_charge_id_invalid(self):

        schema = { 'OfferChargeID':
                       { 'is_offer_charge_id_valid': True, 'type': 'string' }
                 }
        some_offer_charge_id_that_exists_and_is_active = { 'OfferChargeID': '-1' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(some_offer_charge_id_that_exists_and_is_active), False,
                         'An invalid OfferChargeID is not failing validation')


    def test_offer_charge_id_invalid_not_active(self):

        schema = { 'OfferChargeID':
                       { 'is_offer_charge_id_valid': True, 'type': 'string' }
                 }
        some_offer_charge_id_that_exists_and_is_active = { 'OfferChargeID': '710' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(some_offer_charge_id_that_exists_and_is_active), False,
                         'An invalid OfferChargeID is not failing validation')


    def test_offer_code_valid(self):

        schema = { 'OfferCode':
                       { 'is_offer_code_valid': True, 'type': 'string' }
                 }
        some_offer_code_that_exists_and_is_valid = { 'OfferCode': '6A6BCE' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(some_offer_code_that_exists_and_is_valid), True,
                         'A valid OfferCode is failing validation')


    def test_offer_code_invalid(self):

        schema = { 'OfferCode':
                       { 'is_offer_code_valid': True, 'type': 'string' }
                 }
        some_offer_code_that_exists_and_is_valid = { 'OfferCode': 'XXXXXX' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(some_offer_code_that_exists_and_is_valid), False,
                         'An invalid OfferCode is not failing validation')


    def test_offer_code_invalid_not_valid(self):

        schema = { 'OfferCode':
                       { 'is_offer_code_valid': True, 'type': 'string' }
                 }
        some_offer_code_that_exists_and_is_valid = { 'OfferCode': '4074A7' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(some_offer_code_that_exists_and_is_valid), False,
                         'An invalid OfferCode is not failing validation')


    def test_ongoing_frequency_valid(self):

        schema = { 'ongoingFrequency':
                       { 'is_ongoing_frequency_valid': True, 'type': 'string' }
                 }
        ongoing_frequency_1 = { 'ongoingFrequency': '20 days' }
        ongoing_frequency_2 = { 'ongoingFrequency': '24 months' }
        ongoing_frequency_3 = { 'ongoingFrequency': '20 Days' }
        ongoing_frequency_4 = { 'ongoingFrequency': '24 Months' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ongoing_frequency_1), True,
                         'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoing_frequency_2), True,
                         'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoing_frequency_3), True,
                         'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoing_frequency_4), True,
                         'A valid ongoingFrequency is failing validation')


    def test_ongoing_frequency_invalid(self):

        schema = { 'ongoingFrequency':
                       { 'is_ongoing_frequency_valid': True, 'type': 'string' }
                 }
        ongoing_frequency_1 = { 'ongoingFrequency': 'foo' }
        ongoing_frequency_2 = { 'ongoingFrequency': '1 year' }
        ongoing_frequency_3 = { 'ongoingFrequency': '2.5 months' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ongoing_frequency_1), False,
                         'An invalid ongoingFrequency is passing validation')
        self.assertEqual(validator.validate(ongoing_frequency_2), False,
                         'An invalid ongoingFrequency is passing validation')
        self.assertEqual(validator.validate(ongoing_frequency_3), False,
                         'An invalid ongoingFrequency is passing validation')


    def test_ongoing_value_valid(self):

        schema = { 'ongoing_value':
                       { 'is_ongoing_value_valid': True, 'type': 'string' }
                 }
        ongoing_value_1 = { 'ongoing_value': '1%' }
        ongoing_value_2 = { 'ongoing_value': '' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ongoing_value_1), True,
                         'A valid ongoingValue is failing validation')
        self.assertEqual(validator.validate(ongoing_value_2), True,
                         'A valid ongoingValue is failing validation')


    def test_ongoing_value_invalid(self):

        schema = { 'ongoing_value':
                       { 'is_ongoing_value_valid': True, 'type': 'string' }
                 }
        ongoing_value_1 = { 'ongoing_value': 'foo' }
        ongoing_value_2 = { 'ongoing_value': 'f%' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(ongoing_value_1), False,
                         'An invalid ongoingValue is passing validation')
        self.assertEqual(validator.validate(ongoing_value_2), False,
                         'An invalid ongoingValue is passing validation')


    def test_partner_code_valid(self):

        schema = { 'partnerCode':
                       {'is_partner_code_valid': True, 'type': 'string' }
                 }
        partner_code = { 'partnerCode': 'EGR' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(partner_code), True,
                         'A valid partnerCode is failing validation')


    def test_partner_code_invalid(self):

        schema = { 'partnerCode':
                       { 'is_partner_code_valid': True, 'type': 'string' }
                 }
        partner_code = { 'partnerCode': 'foo' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(partner_code), False,
                         'An invalid partnerCode is passing validation')


    def test_premise_type_valid(self):

        schema = { 'premiseType':
                       { 'is_premise_type_valid': True, 'type': 'string' }
                 }
        premise_type = { 'premiseType': 'residential' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(premise_type), True,
                         'A valid premiseType is failing validation')


    def test_premise_type_invalid(self):

        schema = { 'premiseType':
                       { 'is_premise_type_valid': True, 'type': 'string' }
                 }
        premise_type = { 'premiseType': 'foo' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(premise_type), False,
                         'An invalid premiseType is passing validation')


    def test_pricing_term_valid(self):

        schema = { 'pricingTerm':
                       { 'is_pricing_term_valid': True, 'type': 'string'}
                 }
        pricingTerm = { 'pricingTerm': '6' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(pricingTerm), True,
                         'A valid pricingTerm is failing validation')


    def test_pricing_term_invalid(self):

        schema = { 'pricingTerm':
                       { 'is_pricing_term_valid': True, 'type': 'string' }
                 }
        pricing_term_1 = { 'pricingTerm': 'foo' }
        pricing_term_2 = { 'pricingTerm': '2.5' }
        pricing_term_3 = { 'pricingTerm': 'foo 6' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(pricing_term_1), False,
                         'An invalid pricingTerm is passing validation')
        self.assertEqual(validator.validate(pricing_term_2), False,
                         'An invalid pricingTerm is passing validation')
        self.assertEqual(validator.validate(pricing_term_3), False,
                         'An invalid pricingTerm is passing validation')


    def test_promo_code_valid(self):

        schema = { 'promoCode':
                       { 'is_promo_code_valid': True, 'type': 'string' }
                 }
        promo_code = { 'promoCode': '700' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(promo_code), True,
                         'A valid promoCode is failing validation')


    def test_promo_code_invalid(self):

        schema = { 'promoCode':
                       { 'is_promo_code_valid': True, 'type': 'string' }
                 }
        promo_code = { 'promoCode': 'foo' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(promo_code), False,
                         'An invalid promoCode is passing validation')


    def test_rate_valid(self):

        schema = { 'rate':
                       { 'is_rate_valid': True, 'type': 'string' }
                 }
        rate = { 'rate': '0.05' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(rate), True,
                         'A valid rate is failing validation')


    def test_rate_invalid(self):

        schema = { 'rate':
                       { 'is_rate_valid': True, 'type': 'string' }
                 }
        rate_1 = { 'rate': 'foo' }
        rate_2 = { 'rate': '100' }
        rate_3 = { 'rate': '0.039458' }
        rate_4 = { 'rate': '' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(rate_1), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_2), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_3), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_4), False,
                         'An invalid rate is passing validation')


    def test_signup_bonus_valid(self):

        schema = { 'signupBonus':
                       { 'is_signup_bonus_valid': True, 'type': 'string' }
                 }
        signup_bonus = { 'signupBonus': '$50' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(signup_bonus), True,
                         'A valid signupBonus is failing validation')


    def test_signup_bonus_invalid(self):

        schema = { 'signupBonus':
                       { 'is_signup_bonus_valid': True, 'type': 'string' }
                 }
        signup_bonus_1 = { 'signupBonus': 'foo' }
        signup_bonus_2 = { 'signupBonus': '$ 50' }
        signup_bonus_3 = { 'signupBonus': 'words $50' }
        signup_bonus_4 = { 'signupBonus': 'failure$50' }
        signup_bonus_5 = { 'signupBonus': '$50.00' }
        signup_bonus_6 = { 'signupBonus': '$50 words' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(signup_bonus_1), False,
                         'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signup_bonus_2), False,
                         'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signup_bonus_3), False,
                         'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signup_bonus_4), False,
                         'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signup_bonus_5), False,
                         'An invalid signupBonus is passing validation')
        self.assertEqual(validator.validate(signup_bonus_6), False,
                         'An invalid signupBonus is passing validation')


    def test_signup_vesting_valid(self):

        schema = { 'signupVesting':
                       { 'is_signup_vesting_valid': True, 'type': 'string' }
                 }
        signup_vesting_1 = { 'signupVesting': '20 days' }
        signup_vesting_2 = { 'signupVesting': '12 months' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(signup_vesting_1), True,
                         'A valid signupVesting is failing validation')
        self.assertEqual(validator.validate(signup_vesting_2), True,
                         'A valid signupVesting is failing validation')


    def test_signup_vesting_invalid(self):

        schema = {'signupVesting':
                      { 'is_signup_vesting_valid': True, 'type': 'string' }
                 }
        signup_vesting_1 = { 'signupVesting': 'foo' }
        signup_vesting_2 = { 'signupVesting': '1 year' }
        signup_vesting_3 = { 'signupVesting': '2.5 months' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(signup_vesting_1), False,
                         'An invalid signupVesting is passing validation')
        self.assertEqual(validator.validate(signup_vesting_2), False,
                         'An invalid signupVesting is passing validation')
        self.assertEqual(validator.validate(signup_vesting_3), False,
                         'An invalid signupVesting is passing validation')


    def test_sunday_2_cents_valid(self):

        schema = { 'sunday2cents':
                       { 'is_sunday_2_cents_valid': True, 'type': 'string' }
                 }
        sunday_2_cents_1 = { 'sunday2cents': 'Y' }
        sunday_2_cents_2 = { 'sunday2cents': 'N' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(sunday_2_cents_1), True,
                         'A valid sunday2cents is failing validation')
        self.assertEqual(validator.validate(sunday_2_cents_2), True,
                         'A valid sunday2cents is failing validation')


    def test_sunday_2_cents_invalid(self):

        schema = { 'sunday2cents':
                       { 'is_sunday_2_cents_valid': True, 'type': 'string' }
                 }
        sunday_2_cents_1 = { 'sunday2cents': 'foo' }
        sunday_2_cents_2 = { 'sunday2cents': 'fooY' }
        sunday_2_cents_3 = { 'sunday2cents': ' Y' }
        sunday_2_cents_4 = { 'sunday2cents': 'Y ' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(sunday_2_cents_1), False,
                         'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday_2_cents_2), False,
                         'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday_2_cents_3), False,
                         'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday_2_cents_4), False,
                         'An invalid sunday2cents is passing validation')


    def test_vas_code_valid(self):

        schema = { 'vasCode':
                       { 'is_vas_code_valid': True, 'type': 'string' }
                 }
        vas_code = { 'vasCode': '006' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(vas_code), True,
                         'A valid vasCode is failing validation')


    def test_vas_code_invalid(self):

        schema = { 'vasCode':
                       { 'is_vas_code_valid': True, 'type': 'string'}
                 }
        vas_code = { 'vasCode': 'foo' }

        validator = product_validate.ProductValidator(schema)
        validator.allow_unknown = True

        self.assertEqual(validator.validate(vas_code), False,
                         'An invalid vasCode is passing validation')


if __name__ == '__main__':
    unittest.main()

