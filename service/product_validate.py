from domain import product_repository

__author__ = 'rike'

from cerberus import Validator

from decimal import *

class ProductValidator(Validator):

    def _validate_is_valid_brand_slug(self, is_valid_brand_slug, field, value):

        brand_slugs_lower_case = set(k.lower() for k in product_repository.get_brand_slugs())

        if value.lower() not in brand_slugs_lower_case:
            self._error(field, "invalid brand_slug")

    def _validate_is_valid_channel(self, is_valid_channel, field, value):

        channels_lower_case = set(k.lower() for k in product_repository.get_channels())

        if value.lower() not in channels_lower_case:
            self._error(field, "channel does not exist")

    def _validate_is_valid_premiseType(self, is_valid_premiseType, field, value):

        premises_lower_case = set(k.lower() for k in product_repository.get_premiseTypes())

        if value.lower() not in premises_lower_case:
            self._error(field, "premiseType does not exist")

    def _validate_is_valid_partnerCode(self, is_valid_partnerCode, field, value):

        partners_lower_case = set(k.lower() for k in product_repository.get_partnerCodes())

        if value.lower() not in partners_lower_case:
            self._error(field, "partnerCode does not exist")

    def _validate_is_valid_promoCode(self, is_valid_promoCode, field, value):

        promos_lower_case = set(k.lower() for k in product_repository.get_promoCode())

        if value.lower() not in promos_lower_case:
            self._error(field, "promoCode does not exist")

    def _validate_is_valid_pricingTerm(self, is_valid_pricingTerm, field, value):

        if value.isdigit() == False or int(value) < 1:
            self._error(field, "pricingTerm must be a whole number greater than zero")

    def _validate_is_valid_merchandiseVesting(self, is_valid_merchandiseVesting, field, value):

        if value:
            words = value.split(' ')
            accepted_units=["days","months"]

            if words[0].isdigit() == False or words[1] not in accepted_units:
                self._error(field, "merchandiseVesting must be formatted as a number and a unit of time (e.g. - 12 months, 20 days)")

    def _validate_is_valid_signupBonus(self, is_valid_signupBonus, field, value):

        if value:
            words = value.split('$')
            indexOfDollar = value.find('$')

            if indexOfDollar != 0 or words[1].isdigit() == False:
                self._error(field, "signupBonus must be formatted as a dollar amount (e.g. - $50)")

    def _validate_is_valid_signupVesting(self, is_valid_signupVesting, field, value):

        if value:
            words = value.split(' ')
            accepted_units=["days","months"]

            if words[0].isdigit() == False or words[1] not in accepted_units:
                self._error(field, "signupVesting must be formatted as a number and a unit of time (e.g. - 12 months, 20 days)")

    def _validate_is_valid_sunday2cents(self, is_valid_sunday2cents, field, value):

        if value:
            if value not in ("Y","N"):
                self._error(field, "sunday2cents must be formatted as Y for yes, or N for no with no additional characters or spaces")

    def _validate_is_valid_vasCode(self, is_valid_vasCode, field, value):

        vas_lower_case = set(k.lower() for k in product_repository.get_vasCode())

        if value.lower() not in vas_lower_case:
            self._error(field, "vasCode does not exist")

    def _validate_is_valid_rateShownToCustomer(self, is_valid_rateShownToCustomer, field, value):

        if not value or value.count(".") == 0:
            self._error(field, "The rate shown to the customer must be a positive decimal value")
        if len(value) > 7:
            self._error(field, "The rate shown to the customer must be a positive decimal value with up to five digits right of the decimal")
        try:
            if  Decimal(value) < 0.000000:
                self._error(field, "The rate shown to the customer must be a positive decimal value")
        except:
                self._error(field, "The rate shown to the customer must be a positive decimal value")

    def _validate_is_valid_ongoingValue(self, is_valid_ongoingValue, field, value):

        if value:
            if len(value) > 3 or value.count("%") == 0:
                self._error(field, "The ongoing value must be formatted as a percent (e.g. - 1%, 3%, 5%)")
            baseString = value.strip("%")
            if baseString.isnumeric() == False:
                self._error(field, "The ongoing value must be formatted as a percent (e.g. - 1%, 3%, 5%)")

    def _validate_is_valid_ECF(self, is_valid_ECF, field, value):

        if not value or value.count(".") == 0 or value.count("$") != 0:
            self._error(field, "An early cancellation fee must be specified as a monetary amount (e.g. 50.00)")
        if len(value[value.find('.'):len(value)]) > 2: #the substring representing any values to the right of the decimal
            self._error(field, "An early cancellation fee must be specified as a monetary amount with two digits right of the decimal")
        try:
            if  Decimal(value) < 0.000000:
                self._error(field, "The ECF rate must be a positive decimal value")
        except:
                self._error(field, "The ECF rate must be a positive decimal value")



#BrandSlug
#BundleName
#BundleDescription
#Channel
#Commodity
#ECF
#GreenPercentage / VAS_Code
#LockType
#MerchandiseSlug
#MerchandiseVesting
#OngoingFrequency
#OngoingValue
#PartnerCode
#PremiseType
#PricingTerm
#PromoCode
#Rate
#SignupBonus
#SignupVesting
#StateAbbrev
#Sunday2cents
#TermsOfServiceType
#UtilityAbbrev
#UtilityCode