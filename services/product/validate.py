__author__ = 'rike'

from cerberus import Validator
from domain.product import repository

class ProductValidator(Validator):

    def _validate_is_valid_brand_slug(self, is_valid_brand_slug, field, value):
        product_repository = repository.Repository()
        brand_slugs = product_repository.get_bland_slugs()

        if value not in brand_slugs:
            self._error(field, "invalid brand_slug")

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