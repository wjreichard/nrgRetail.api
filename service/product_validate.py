from decimal import *
from domain import product_repository as repo
from cerberus import Validator



class ProductValidator(Validator):


    def _validate_is_brand_slug_valid(self, is_brand_slug_valid, field, value):

        brand_slugs_lower_case = set(k.lower() for k in repo.get_brand_slugs())

        if value.lower() not in brand_slugs_lower_case:
            self._error(field, "invalid brand_slug.")


    def _validate_is_channel_valid(self, is_channel_valid, field, value):

        if value.lower() not in repo.get_channels():
            self._error(field, "channel does not exist.")


    def _validate_is_default_bundle_valid(self, is_default_bundle_valid, field, value):

        if value.strip().lower() not in ("true", "false", "1", "0"):
                self._error(field, "default bundle is not a boolean.")


    def _validate_is_ecf_valid(self, is_ecf_valid, field, value):

        if not value or value.count(".") == 0 or value.count("$") != 0:
            self._error(field, "An early cancellation fee must be specified as a monetary amount (e.g. 50.00).")
        if len(value[value.find('.')+1:len(value)]) > 2: # substring representing digits to the right of the decimal
            self._error(field, """
                                    An early cancellation fee must be specified as a
                                    monetary amount with two digits right of the decimal.""")
        try:
            if Decimal(value) < 0.000000:
                self._error(field, "The ECF rate must be a positive decimal value.")
        except:
                self._error(field, "The ECF rate must be a positive decimal value.")


    def _validate_is_merchandise_vesting_valid(self, is_merchandise_vesting_valid, field, value):

        if value:
            words = value.split(' ')
            accepted_units=["days","months"]

            if words[0].isdigit() == False or words[1].lower() not in accepted_units:
                self._error(field, """
                    merchandiseVesting must be formatted as a number and a unit of time (e.g. - 12 months, 20 days).""")


    def _validate_is_offer_charge_id_valid(self, is_offer_charge_id_valid, field, value):

        if repo.does_active_offer_charge_id_exist(value) is False:
            self._error(field, "OfferChargeID does not exist or is not active.")


    def _validate_is_offer_code_valid(self, is_offer_code_valid, field, value):

        if repo.does_valid_offer_code_exist(value) is False:
            self._error(field, "OfferCode does not exist or is not valid.")

    def _validate_is_ongoing_frequency_valid(self, is_ongoing_frequency_valid, field, value):

        if value:
            words = value.split(' ')
            accepted_units=["days","months"]

            if words[0].isdigit() == False or words[1].lower() not in accepted_units:
                self._error(field, """
                                        ongoingFrequency must be formatted as a number
                                        and a unit of time (e.g. - 12 months, 20 days).""")


    def _validate_is_ongoing_value_valid(self, is_ongoing_value_valid, field, value):

        if value:
            if len(value) > 3 or value.count("%") == 0:
                self._error(field, "The ongoing value must be formatted as a percent (e.g. - 1%, 3%, 5%).")
            baseString = value.strip("%")
            if baseString.isnumeric() == False:
                self._error(field, "The ongoing value must be formatted as a percent (e.g. - 1%, 3%, 5%).")


    def _validate_is_partner_code_valid(self, is_partner_code_valid, field, value):

        partners_lower_case = set(k.lower() for k in repo.get_partner_codes())

        if value.lower() not in partners_lower_case:
            self._error(field, "partnerCode does not exist.")


    def _validate_is_premise_type_valid(self, is_premise_type_valid, field, value):

        premises_lower_case = set(k.lower() for k in repo.get_premise_types())

        if value.lower() not in premises_lower_case:
            self._error(field, "premiseType does not exist.")


    def _validate_is_promo_code_valid(self, is_promo_code_valid, field, value):

        promos_lower_case = set(k.lower() for k in repo.get_promo_code())

        if value.lower() not in promos_lower_case:
            self._error(field, "promoCode does not exist.")


    def _validate_is_pricing_term_valid(self, is_pricing_term_valid, field, value):

        if value.isdigit() == False or int(value) < 1:
            self._error(field, "pricingTerm must be a whole number greater than zero.")


    def _validate_is_rate_valid(self, is_rate_valid, field, value):

        if not value or value.count(".") == 0:
            self._error(field, "The rate shown to the customer must be a positive decimal value.")
        if len(value) > 7:
            self._error(field, """
                        The rate shown to the customer must be a positive decimal value with
                        up to five digits right of the decimal.""")
        try:
            if  Decimal(value) < 0.000000:
                self._error(field, "The rate shown to the customer must be a positive decimal value.")
        except:
                self._error(field, "The rate shown to the customer must be a positive decimal value.")


    def _validate_is_signup_bonus_valid(self, is_signup_bonus_valid, field, value):

        if value:
            words = value.split('$')
            indexOfDollar = value.find('$')

            if indexOfDollar != 0 or words[1].isdigit() == False:
                self._error(field, "signupBonus must be formatted as a dollar amount (e.g. - $50).")


    def _validate_is_signup_vesting_valid(self, is_signup_vesting_valid, field, value):

        if value:
            words = value.split(' ')
            accepted_units=["days","months"]

            if words[0].isdigit() == False or words[1].lower() not in accepted_units:
                self._error(field, """
                        signupVesting must be formatted as a number and a unit of time (e.g. - 12 months, 20 days).""")


    def _validate_is_sunday_2_cents_valid(self, is_sunday_2_cents_valid, field, value):

        if value:
            if value not in ("Y","N"):
                self._error(field, """
                                        sunday2cents must be formatted as Y for yes, or N for no
                                        with no additional characters or spaces.
                                   """)


    def _validate_is_utility_brand_state_valid(self, is_utility_brand_state_valid, field, value):

        print(value)

        #Define access to individual fields in the dict
        utilityBrands = repo.get_utility_brands()

        #check if exists by comparison of the fields to the utilityBrandState getter
        if not any( value['StateAbbrev'] == d['State']
                    and value['UtilityCode'] == d['UtilityCode']
                    and value['BrandSlug'] == d['BrandSlug']
                    and value['Commodity'] == d['Commodity']
                    for d in utilityBrands):
            self._error(field, "The utility/state/brand combination supplied is invalid.")


    def _validate_is_vas_code_valid(self, is_vas_code_valid, field, value):

        vas_lower_case = set(k.lower() for k in repo.get_vas_code())

        if value.lower() not in vas_lower_case:
            self._error(field, "vasCode does not exist.")
