from service import individual_product_validator
import unittest


class TestValidateProductIndividualField(unittest.TestCase):
    def test_brand_slug_valid(self):
        schema = {'BrandSlug':
                      {'is_brand_slug_valid': True, 'type': 'string'}
        }
        brand_slug = {'BrandSlug': 'nrg_residential'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(brand_slug), True,
                         'A valid brand_slug is failing validation')


    def test_brand_slug_does_not_exist(self):
        schema = {'BrandSlug':
                      {'is_brand_slug_valid': True, 'type': 'string'}
        }
        brand_slug = {'BrandSlug': 'foo'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(brand_slug), False,
                         'An invalid brand_slug is passing validation')


    def test_channel_valid(self):
        schema = {'Channel':
                      {'is_channel_valid': True, 'type': 'string'}
        }
        channel_1 = {'Channel': 'inbound_telemarketing'}
        channel_2 = {'Channel': 'web'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(channel_1), True,
                         'A valid channel is failing validation')
        self.assertEqual(validator.validate(channel_2), True,
                         'A valid channel is failing validation')


    def test_channel_invalid(self):
        schema = {'Channel':
                      {'is_channel_valid': True, 'type': 'string'}
        }
        channel_1 = {'Channel': 'foo'}
        channel_2 = {'Channel': 'AQ'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(channel_1), False,
                         'An invalid channel is passing validation')
        self.assertEqual(validator.validate(channel_2), False,
                         'An invalid channel is passing validation')


    def test_default_bundle_valid(self):
        schema = {'DefaultBundle':
                      {'is_default_bundle_valid': True, 'type': 'string'}
        }
        channel_1 = {'DefaultBundle': 'True'}
        channel_2 = {'DefaultBundle': 'False'}
        channel_3 = {'DefaultBundle': '1'}
        channel_4 = {'DefaultBundle': '0'}
        channel_5 = {'DefaultBundle': 'tRue'}
        channel_6 = {'DefaultBundle': 'fAlsE'}

        validator = individual_product_validator.ProductValidator(schema)

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
        schema = {'DefaultBundle':
                      {'is_default_bundle_valid': True, 'type': 'string'}
        }

        channel_1 = {'DefaultBundle': ''}
        channel_2 = {'DefaultBundle': 'foo'}
        channel_3 = {'DefaultBundle': 1}
        channel_4 = {'DefaultBundle': 0}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(channel_1), False,
                         'An invalid default bundle is passing validation')
        self.assertEqual(validator.validate(channel_2), False,
                         'An invalid default bundle is passing validation')
        self.assertEqual(validator.validate(channel_3), False,
                         'An invalid default bundle is passing validation')
        self.assertEqual(validator.validate(channel_4), False,
                         'An invalid default bundle is passing validation')


    def test_lock_type_valid(self):
        schema = {'LockType':
                      {'is_lock_type_valid': True, 'type': 'string', 'required': True}
        }
        lock_type_1 = {'LockType': 'Intro'}
        lock_type_2 = {'LockType': 'Contract'}
        lock_type_3 = {'LockType': 'Indexed'}
        lock_type_4 = {'LockType': 'iNtRo'}
        lock_type_5 = {'LockType': 'cOnTrAcT'}
        lock_type_6 = {'LockType': 'iNdExEd'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(lock_type_1), True,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_2), True,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_3), True,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_4), True,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_5), True,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_6), True,
                         'An invalid LockType is passing validation')


    def test_lock_type_invalid(self):
        schema = {'LockType':
                      {'is_lock_type_valid': True, 'type': 'string', 'required': True}
        }
        lock_type_1 = {'LockType': ''}
        lock_type_2 = {'LockType': 'foo'}
        lock_type_3 = {'LockType': 'Index'}
        lock_type_4 = {'LockType': 'Introduction'}
        lock_type_5 = {'LockType': 'Variable'}
        lock_type_6 = {'LockType': 'variable'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(lock_type_1), False,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_2), False,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_3), False,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_4), False,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_5), False,
                         'An invalid LockType is passing validation')
        self.assertEqual(validator.validate(lock_type_6), False,
                         'An invalid LockType is passing validation')


    def test_merchandise_vesting_valid(self):
        schema = {'merchandiseVesting':
                      {'is_merchandise_vesting_valid': True, 'type': 'string'}
        }
        merchandise_vesting_1 = {'merchandiseVesting': '20 days'}
        merchandise_vesting_2 = {'merchandiseVesting': '12 months'}
        merchandise_vesting_3 = {'merchandiseVesting': '20 Days'}
        merchandise_vesting_4 = {'merchandiseVesting': '12 Months'}

        validator = individual_product_validator.ProductValidator(schema)

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
                      {'is_merchandise_vesting_valid': True, 'type': 'string'}
        }
        merchandise_vesting_1 = {'merchandiseVesting': 'foo'}
        merchandise_vesting_2 = {'merchandiseVesting': '1 year'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(merchandise_vesting_1), False,
                         'An invalid merchandiseVesting is passing validation')
        self.assertEqual(validator.validate(merchandise_vesting_2), False,
                         'An invalid merchandiseVesting is passing validation')


    def test_ongoing_frequency_valid(self):
        schema = {'ongoingFrequency':
                      {'is_ongoing_frequency_valid': True, 'type': 'string'}
        }
        ongoing_frequency_1 = {'ongoingFrequency': '20 days'}
        ongoing_frequency_2 = {'ongoingFrequency': '24 months'}
        ongoing_frequency_3 = {'ongoingFrequency': '20 Days'}
        ongoing_frequency_4 = {'ongoingFrequency': '24 Months'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(ongoing_frequency_1), True,
                         'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoing_frequency_2), True,
                         'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoing_frequency_3), True,
                         'A valid ongoingFrequency is failing validation')
        self.assertEqual(validator.validate(ongoing_frequency_4), True,
                         'A valid ongoingFrequency is failing validation')


    def test_ongoing_frequency_invalid(self):
        schema = {'ongoingFrequency':
                      {'is_ongoing_frequency_valid': True, 'type': 'string'}
        }
        ongoing_frequency_1 = {'ongoingFrequency': 'foo'}
        ongoing_frequency_2 = {'ongoingFrequency': '1 year'}
        ongoing_frequency_3 = {'ongoingFrequency': '2.5 months'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(ongoing_frequency_1), False,
                         'An invalid ongoingFrequency is passing validation')
        self.assertEqual(validator.validate(ongoing_frequency_2), False,
                         'An invalid ongoingFrequency is passing validation')
        self.assertEqual(validator.validate(ongoing_frequency_3), False,
                         'An invalid ongoingFrequency is passing validation')


    def test_ongoing_value_valid(self):
        schema = {'ongoing_value':
                      {'is_ongoing_value_valid': True, 'type': 'string'}
        }
        ongoing_value_1 = {'ongoing_value': '1%'}
        ongoing_value_2 = {'ongoing_value': ''}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(ongoing_value_1), True,
                         'A valid ongoingValue is failing validation')
        self.assertEqual(validator.validate(ongoing_value_2), True,
                         'A valid ongoingValue is failing validation')


    def test_ongoing_value_invalid(self):
        schema = {'ongoing_value':
                      {'is_ongoing_value_valid': True, 'type': 'string'}
        }
        ongoing_value_1 = {'ongoing_value': 'foo'}
        ongoing_value_2 = {'ongoing_value': 'f%'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(ongoing_value_1), False,
                         'An invalid ongoingValue is passing validation')
        self.assertEqual(validator.validate(ongoing_value_2), False,
                         'An invalid ongoingValue is passing validation')


    def test_partner_code_valid(self):
        schema = {'partnerCode':
                      {'is_partner_code_valid': True, 'type': 'string'}
        }
        partner_code = {'partnerCode': 'EGR'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(partner_code), True,
                         'A valid partnerCode is failing validation')


    def test_partner_code_invalid(self):
        schema = {'partnerCode':
                      {'is_partner_code_valid': True, 'type': 'string'}
        }
        partner_code = {'partnerCode': 'foo'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(partner_code), False,
                         'An invalid partnerCode is passing validation')


    def test_premise_type_valid(self):
        schema = {'premiseType':
                      {'is_premise_type_valid': True, 'type': 'string'}
        }
        premise_type = {'premiseType': 'residential'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(premise_type), True,
                         'A valid premiseType is failing validation')


    def test_premise_type_invalid(self):
        schema = {'premiseType':
                      {'is_premise_type_valid': True, 'type': 'string'}
        }
        premise_type = {'premiseType': 'foo'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(premise_type), False,
                         'An invalid premiseType is passing validation')


    def test_pricing_term_valid(self):
        schema = {'pricingTerm':
                      {'is_pricing_term_valid': True, 'type': 'string'}
        }
        pricingTerm = {'pricingTerm': '6'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(pricingTerm), True,
                         'A valid pricingTerm is failing validation')


    def test_pricing_term_invalid(self):
        schema = {'pricingTerm':
                      {'is_pricing_term_valid': True, 'type': 'string'}
        }
        pricing_term_1 = {'pricingTerm': 'foo'}
        pricing_term_2 = {'pricingTerm': '2.5'}
        pricing_term_3 = {'pricingTerm': 'foo 6'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(pricing_term_1), False,
                         'An invalid pricingTerm is passing validation')
        self.assertEqual(validator.validate(pricing_term_2), False,
                         'An invalid pricingTerm is passing validation')
        self.assertEqual(validator.validate(pricing_term_3), False,
                         'An invalid pricingTerm is passing validation')


    def test_promo_code_valid(self):
        schema = {'promoCode':
                      {'is_promo_code_valid': True, 'type': 'string'}
        }
        promo_code = {'promoCode': '700'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(promo_code), True,
                         'A valid promoCode is failing validation')


    def test_promo_code_invalid(self):
        schema = {'promoCode':
                      {'is_promo_code_valid': True, 'type': 'string'}
        }
        promo_code = {'promoCode': 'foo'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(promo_code), False,
                         'An invalid promoCode is passing validation')


    def test_rate_valid(self):
        schema = {'rate':
                      {'is_rate_valid': True, 'type': 'string'}
        }
        rate_1 = {'rate': '0.5'}
        rate_2 = {'rate': '0.05'}
        rate_3 = {'rate': '0.005'}
        rate_4 = {'rate': '0.0005'}
        rate_5 = {'rate': '0.00005'}
        rate_6 = {'rate': '.5'}
        rate_7 = {'rate': '.05'}
        rate_8 = {'rate': '.005'}
        rate_9 = {'rate': '.0005'}
        rate_10 = {'rate': '.00005'}
        rate_11 = {'rate': '1.00001'}
        rate_12 = {'rate': '12345.12345'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(rate_1), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_2), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_3), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_4), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_5), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_6), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_7), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_8), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_9), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_10), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_11), True,
                         'A valid rate is failing validation')
        self.assertEqual(validator.validate(rate_12), True,
                         'A valid rate is failing validation')


    def test_rate_invalid(self):
        schema = {'rate':
                      {'is_rate_valid': True, 'type': 'string'}
        }
        rate_1 = {'rate': 'foo'}
        rate_2 = {'rate': '100'}
        rate_3 = {'rate': '0.039458'}
        rate_4 = {'rate': ''}
        rate_5 = {'rate': '.'}
        rate_6 = {'rate': '0.'}
        rate_7 = {'rate': '.0'}
        rate_8 = {'rate': '0.0'}
        rate_9 = {'rate': '0.00'}
        rate_10 = {'rate': '0.000'}
        rate_11 = {'rate': '0.0000'}
        rate_12 = {'rate': '0.00000'}
        rate_13 = {'rate': '0.000000'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(rate_1), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_2), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_3), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_4), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_5), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_6), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_7), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_8), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_9), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_10), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_11), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_12), False,
                         'An invalid rate is passing validation')
        self.assertEqual(validator.validate(rate_13), False,
                         'An invalid rate is passing validation')


    def test_signup_bonus_valid(self):
        schema = {'signupBonus':
                      {'is_signup_bonus_valid': True, 'type': 'string'}
        }
        signup_bonus = {'signupBonus': '$50'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(signup_bonus), True,
                         'A valid signupBonus is failing validation')


    def test_signup_bonus_invalid(self):
        schema = {'signupBonus':
                      {'is_signup_bonus_valid': True, 'type': 'string'}
        }
        signup_bonus_1 = {'signupBonus': 'foo'}
        signup_bonus_2 = {'signupBonus': '$ 50'}
        signup_bonus_3 = {'signupBonus': 'words $50'}
        signup_bonus_4 = {'signupBonus': 'failure$50'}
        signup_bonus_5 = {'signupBonus': '$50.00'}
        signup_bonus_6 = {'signupBonus': '$50 words'}

        validator = individual_product_validator.ProductValidator(schema)

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
        schema = {'signupVesting':
                      {'is_signup_vesting_valid': True, 'type': 'string'}
        }
        signup_vesting_1 = {'signupVesting': '20 days'}
        signup_vesting_2 = {'signupVesting': '12 months'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(signup_vesting_1), True,
                         'A valid signupVesting is failing validation')
        self.assertEqual(validator.validate(signup_vesting_2), True,
                         'A valid signupVesting is failing validation')


    def test_signup_vesting_invalid(self):
        schema = {'signupVesting':
                      {'is_signup_vesting_valid': True, 'type': 'string'}
        }
        signup_vesting_1 = {'signupVesting': 'foo'}
        signup_vesting_2 = {'signupVesting': '1 year'}
        signup_vesting_3 = {'signupVesting': '2.5 months'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(signup_vesting_1), False,
                         'An invalid signupVesting is passing validation')
        self.assertEqual(validator.validate(signup_vesting_2), False,
                         'An invalid signupVesting is passing validation')
        self.assertEqual(validator.validate(signup_vesting_3), False,
                         'An invalid signupVesting is passing validation')


    def test_sunday_2_cents_valid(self):
        schema = {'sunday2cents':
                      {'is_sunday_2_cents_valid': True, 'type': 'string'}
        }
        sunday_2_cents_1 = {'sunday2cents': 'Y'}
        sunday_2_cents_2 = {'sunday2cents': 'N'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(sunday_2_cents_1), True,
                         'A valid sunday2cents is failing validation')
        self.assertEqual(validator.validate(sunday_2_cents_2), True,
                         'A valid sunday2cents is failing validation')


    def test_sunday_2_cents_invalid(self):
        schema = {'sunday2cents':
                      {'is_sunday_2_cents_valid': True, 'type': 'string'}
        }
        sunday_2_cents_1 = {'sunday2cents': 'foo'}
        sunday_2_cents_2 = {'sunday2cents': 'fooY'}
        sunday_2_cents_3 = {'sunday2cents': ' Y'}
        sunday_2_cents_4 = {'sunday2cents': 'Y '}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(sunday_2_cents_1), False,
                         'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday_2_cents_2), False,
                         'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday_2_cents_3), False,
                         'An invalid sunday2cents is passing validation')
        self.assertEqual(validator.validate(sunday_2_cents_4), False,
                         'An invalid sunday2cents is passing validation')


    def test_terms_of_service_type_valid(self):
        schema = {'TermsOfServiceType':
                      {'is_terms_of_service_type_valid': True, 'type': 'string', 'required': True}
        }
        terms_of_service_type_1 = {'TermsOfServiceType': 'Fixed'}
        terms_of_service_type_2 = {'TermsOfServiceType': 'Variable'}
        terms_of_service_type_3 = {'TermsOfServiceType': 'Indexed'}
        terms_of_service_type_4 = {'TermsOfServiceType': 'fIxEd'}
        terms_of_service_type_5 = {'TermsOfServiceType': 'vArIaBlE'}
        terms_of_service_type_6 = {'TermsOfServiceType': 'iNdExEd'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(terms_of_service_type_1), True,
                         'An invalid TermsOfServiceType is passing validation')
        self.assertEqual(validator.validate(terms_of_service_type_2), True,
                         'An invalid TermsOfServiceType is passing validation')
        self.assertEqual(validator.validate(terms_of_service_type_3), True,
                         'An invalid TermsOfServiceType is passing validation')
        self.assertEqual(validator.validate(terms_of_service_type_4), True,
                         'An invalid TermsOfServiceType is passing validation')
        self.assertEqual(validator.validate(terms_of_service_type_5), True,
                         'An invalid TermsOfServiceType is passing validation')
        self.assertEqual(validator.validate(terms_of_service_type_6), True,
                         'An invalid TermsOfServiceType is passing validation')


    def test_terms_of_service_type_invalid(self):
        schema = {'TermsOfServiceType':
                      {'is_terms_of_service_type_valid': True, 'type': 'string', 'required': True}
        }
        terms_of_service_type_1 = {'TermsOfServiceType': ''}
        terms_of_service_type_2 = {'TermsOfServiceType': 'Var'}
        terms_of_service_type_3 = {'TermsOfServiceType': 'Index'}
        terms_of_service_type_4 = {'TermsOfServiceType': 'foo'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(terms_of_service_type_1), False,
                         'An invalid TermsOfServiceType is passing validation')
        self.assertEqual(validator.validate(terms_of_service_type_2), False,
                         'An invalid TermsOfServiceType is passing validation')
        self.assertEqual(validator.validate(terms_of_service_type_3), False,
                         'An invalid TermsOfServiceType is passing validation')
        self.assertEqual(validator.validate(terms_of_service_type_4), False,
                         'An invalid TermsOfServiceType is passing validation')


    def test_vas_code_valid(self):
        schema = {'vasCode':
                      {'is_vas_code_valid': True, 'type': 'string'}
        }
        vas_code = {'vasCode': '006'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(vas_code), True,
                         'A valid vasCode is failing validation')


    def test_vas_code_invalid(self):
        schema = {'vasCode':
                      {'is_vas_code_valid': True, 'type': 'string'}
        }
        vas_code = {'vasCode': 'foo'}

        validator = individual_product_validator.ProductValidator(schema)

        self.assertEqual(validator.validate(vas_code), False,
                         'An invalid vasCode is passing validation')


if __name__ == '__main__':
    unittest.main()