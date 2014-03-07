__author__ = 'rike'

from cerberus import Validator
from domain.product import repository


class ProductValidator(Validator):

    def _validate_is_valid_brand_slug(self, is_valid_brand_slug, field, value):

        #product_repository = repository.Repository()
        brand_slugs_lower_case = set(k.lower() for k in repository.get_bland_slugs())

        if value.lower() not in brand_slugs_lower_case:
            self._error(field, "invalid brand_slug")

    def _validate_is_valid_channel(self, is_valid_channel, field, value):

        #product_repository = repository.Repository()
        channels_lower_case = set(k.lower() for k in repository.get_channels())

        if value.lower() not in channels_lower_case:
            self._error(field, "invalid channel")


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