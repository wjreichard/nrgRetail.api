import logging
from config import config
from domain import product_validation_repository as repo
from cerberus import Validator


logger = logging.getLogger('api')


class ProductValidator(Validator):

    brand_slugs = set(b.lower() for b in repo.get_brand_slugs())
    channels = repo.get_channels()
    partners_codes = set(p.lower() for p in repo.get_partner_codes())
    premises_types = set(p.lower() for p in repo.get_premise_types())
    promo_codes = set(p.lower() for p in repo.get_promo_code())
    vas_codes = set(v.lower() for v in repo.get_vas_code())

    def _validate_is_brand_slug_valid(self, is_brand_slug_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_brand_slug_valid(): start.')

        if value.lower() not in self.brand_slugs:
            self._error(field, "invalid brand_slug.")


    def _validate_is_channel_valid(self, is_channel_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_channel_valid(): start.')

        if value.lower() not in self.channels:
            self._error(field, "channel does not exist.")


    def _validate_is_default_bundle_valid(self, is_default_bundle_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_default_bundle_valid(): start.')

        if value.strip().lower() not in ("true", "false", "1", "0"):
            self._error(field, "default bundle is not a boolean.")


    def _validate_is_lock_type_valid(self, is_lock_type_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_lock_type_valid(): start.')

        if not value.lower() in [l.lower() for l in config.LockTypes]:
            self._error(field, "A Lock Type must be: Intro, Contract or Indexed.")


    def _validate_is_merchandise_vesting_valid(self, is_merchandise_vesting_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_merchandise_vesting_valid(): start.')

        if value:
            words = value.split(' ')
            accepted_units = ["days", "months"]

            if len(words) is not 2 or words[0].isdigit() == False or words[1].lower() not in accepted_units:
                self._error(field, "merchandiseVesting must be a number and a unit of time (e.g. 12 months, 20 days).")


    def _validate_is_ongoing_frequency_valid(self, is_ongoing_frequency_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_ongoing_frequency_valid(): start.')

        if value:
            words = value.split(' ')
            accepted_units = ["days", "months"]

            if len(words) is not 2 or words[0].isdigit() == False or words[1].lower() not in accepted_units:
                self._error(field, "ongoingFrequency must be a number and a unit of time (e.g. 12 months, 20 days).")


    def _validate_is_ongoing_value_valid(self, is_ongoing_value_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_ongoing_value_valid(): start.')

        if value:
            if len(value) > 3 or value.count("%") == 0:
                self._error(field, "The ongoing value must be formatted as a percent (e.g. - 1%, 3%, 5%).")
            baseString = value.strip("%")
            if baseString.isnumeric() == False:
                self._error(field, "The ongoing value must be formatted as a percent (e.g. - 1%, 3%, 5%).")


    def _validate_is_partner_code_valid(self, is_partner_code_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_partner_code_valid(): start.')

        if value.lower() not in self.partners_codes:
            self._error(field, "partnerCode does not exist.")


    def _validate_is_premise_type_valid(self, is_premise_type_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_premise_type_valid(): start.')

        if value.lower() not in self.premises_types:
            self._error(field, "premiseType does not exist.")


    def _validate_is_promo_code_valid(self, is_promo_code_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_promo_code_valid(): start.')

        if value.lower() not in self.promo_codes:
            self._error(field, "promoCode does not exist.")


    def _validate_is_pricing_term_valid(self, is_pricing_term_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_pricing_term_valid(): start.')

        if value.isdigit() == False or int(value) < 1:
            self._error(field, "pricingTerm must be a whole number greater than zero.")


    def _validate_is_rate_valid(self, is_rate_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_rate_valid(): start.')

        if config.regex_rate.match(value) is None:
            self._error(field, 'The rate shown to the customer must be a positive decimal value with '
                               'up to five digits right of the decimal.')


    def _validate_is_signup_bonus_valid(self, is_signup_bonus_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_signup_bonus_valid(): start.')

        if value:
            words = value.split('$')
            indexOfDollar = value.find('$')

            if indexOfDollar != 0 or words[1].isdigit() == False:
                self._error(field, "signupBonus must be formatted as a dollar amount (e.g. - $50).")


    def _validate_is_signup_vesting_valid(self, is_signup_vesting_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_signup_vesting_valid(): start.')

        if value:
            words = value.split(' ')
            accepted_units = ["days", "months"]

            if len(words) is not 2 or words[0].isdigit() == False or words[1].lower() not in accepted_units:
                self._error(field, "signupVesting must be a number and a unit of time (e.g. 12 months, 20 days).")


    def _validate_is_sunday_2_cents_valid(self, is_sunday_2_cents_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_sunday_2_cents_valid(): start.')

        if value:
            if value not in ("Y", "N"):
                self._error(field, """
                                        sunday2cents must be formatted as Y for yes, or N for no
                                        with no additional characters or spaces.
                                   """)


    def _validate_is_terms_of_service_type_valid(self, is_terms_of_service_type_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_terms_of_service_type_valid(): start.')

        if not value.lower() in [t.lower() for t in config.TermsOfServiceTypes]:
            self._error(field, "A Terms Of Service Type must be: Fixed, Variable, Indexed.")


    def _validate_is_vas_code_valid(self, is_vas_code_valid, field, value):

        logger.debug('product_validate_individual_field._validate_is_vas_code_valid(): start.')

        if value.lower() not in self.vas_codes:
            self._error(field, "VAS_Code does not exist.")
