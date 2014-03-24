import ast, logging
from config import config
from domain import product_validation_repository as repo


logger = logging.getLogger('api')

brand_commodity_state_utility_abbreviation_utility_codes = \
    repo.get_brand_commodity_state_utility_abbreviation_utility_code()
partner_promotion_codes = repo.get_partner_promotion_codes()
vas_code_percentages = repo.get_vas_code_percentages()


def validate(products):
    logger.debug('product_catalog.validate(): start.')

    products = check_bundle_description_bundle_name_bundle_slug_combination(products)
    products = check_brandslug_commodity_state_utility_abbreviation_utility_code_combination(products)
    products = check_ecf_terms_of_service_type_non_variable_combination(products)
    products = check_ecf_terms_of_service_type_variable_combination(products)
    products = check_green_percentage_vas_code_pair_combination(products)
    products = check_green_percentage_vas_code_match_combination(products)
    products = check_partner_code_promo_code_combination(products)
    products = check_merchandise_merchandise_slug_merchandise_vesting_combination(products)
    products = check_ongoing_frequency_ongoing_value_combination(products)
    products = check_signup_bonus_signup_vesting_combination(products)

    return products


def check_bundle_description_bundle_name_bundle_slug_combination(products):
    for p in products:
        if not is_bundle_description_bundle_name_bundle_slug_valid(p['BundleDescription'],
                                                                   p['BundleName'],
                                                                   p['BundleSlug']):
            e = ast.literal_eval(p['Errors'])
            e.update({"BrandDescription-BundleName-BundleSlug": "must be a complete set."})
            p['Errors'] = str(e)

    return products


def check_brandslug_commodity_state_utility_abbreviation_utility_code_combination(products):
    for p in products:
        if not is_brand_commodity_state_utility_abbreviation_utility_code_valid(p['BrandSlug'],
                                                                                p['Commodity'],
                                                                                p['State'],
                                                                                p['UtilityAbbrev'],
                                                                                p['UtilityCode']):
            e = ast.literal_eval(p['Errors'])
            e.update({"BrandSlug-Commodity-State-UtilityAbbrev-UtilityCode": "must be a valid set."})
            p['Errors'] = str(e)

    return products


def check_ecf_terms_of_service_type_non_variable_combination(products):
    for p in products:
        if p['TermsOfServiceType'] != config.TermsOfServiceTypes.Variable:
            if not is_ecf_terms_of_service_type_non_variable_valid(p['ECF']):
                e = ast.literal_eval(p['Errors'])
                e.update({"ECF-TermsOfServiceType Non-Variable": "TOS must have an ECF, "
                    "a positive monetary amount (e.g. $50.00 / 550.00)."})

                p['Errors'] = str(e)

    return products


def check_ecf_terms_of_service_type_variable_combination(products):
    for p in products:
        if p['TermsOfServiceType'] == config.TermsOfServiceTypes.Variable:
            if not is_ecf_terms_of_service_type_variable_valid(p['ECF']):
                e = ast.literal_eval(p['Errors'])
                e.update({"ECF-TermsOfServiceType Variable": "TOS can not have an ECF."})
                p['Errors'] = str(e)

    return products


def check_green_percentage_vas_code_match_combination(products):
    for p in products:
        if not is_green_percentage_vas_code_match_valid(p['GreenPercentage'], p['VAS_Code']):
            e = ast.literal_eval(p['Errors'])
            e.update({"GreenPercentage-VAS_Code Pair": "must be a valid pair"})
            p['Errors'] = str(e)

    return products


def check_green_percentage_vas_code_pair_combination(products):
    for p in products:
        if not is_green_percentage_vas_code_pair_valid(p['GreenPercentage'], p['VAS_Code']):
            e = ast.literal_eval(p['Errors'])
            e.update({"GreenPercentage-VAS_Code Match": "must be a complete pair"})
            p['Errors'] = str(e)

    return products


def check_merchandise_merchandise_slug_merchandise_vesting_combination(products):
    for p in products:
        if not is_merchandise_merchandise_slug_merchandise_vesting_valid(p['Merchandise'],
                                                                         p['MerchandiseSlug'],
                                                                         p['MerchandiseVesting']):
            e = ast.literal_eval(p['Errors'])
            e.update({"Merchandise-MerchandiseSlug-MerchandiseVesting": "must be a complete set."})
            p['Errors'] = str(e)

    return products


def check_ongoing_frequency_ongoing_value_combination(products):
    for p in products:
        if not is_ongoing_frequency_ongoing_value_valid(p['OngoingFrequency'], p['OngoingValue']):
            e = ast.literal_eval(p['Errors'])
            e.update({"OngoingFrequency-OngoingValue": "must be a complete pair."})
            p['Errors'] = str(e)

    return products


def check_partner_code_promo_code_combination(products):
    for p in products:
        if not is_partner_code_promo_code_valid(p['PartnerCode'], p['PromoCode']):
            e = ast.literal_eval(p['Errors'])
            e.update({"PartnerCode-PromoCode": "combination is not valid."})
            p['Errors'] = str(e)

    return products


def check_signup_bonus_signup_vesting_combination(products):
    for p in products:
        if not is_signup_bonus_signup_vesting_valid(p['SignupBonus'], p['SignupVesting']):
            e = ast.literal_eval(p['Errors'])
            e.update({"SignupBonus-SignupVesting": "must be a compete pair."})
            p['Errors'] = str(e)

    return products


def is_bundle_description_bundle_name_bundle_slug_valid(bundle_description, bundle_name, bundle_slug):
    valid = False

    if len(bundle_description) is 0 and len(bundle_name) is 0 and len(bundle_slug) is 0:
        valid = True

    if len(bundle_description) is not 0 and len(bundle_name) is not 0 and len(bundle_slug) is not 0:
        valid = True

    return valid


def is_brand_commodity_state_utility_abbreviation_utility_code_valid(brand,
                                                                     commodity,
                                                                     state,
                                                                     utility_abbreviation,
                                                                     utility_code):
    logger.debug('product_validate_multiple_fields.is_brand_commodity_state_utility_valid(): start.')

    search = {}
    search['BrandSlug'] = brand.lower()
    search['Commodity'] = commodity.lower()
    search['State'] = state.lower()
    search['UtilityAbbrev'] = utility_abbreviation.lower()
    search['UtilityCode'] = utility_code

    return search in brand_commodity_state_utility_abbreviation_utility_codes


def is_ecf_terms_of_service_type_non_variable_valid(ecf):

    return config.regex_currency.match(ecf) is not None


def is_ecf_terms_of_service_type_variable_valid(ecf):

    return not bool(ecf)


def is_green_percentage_vas_code_match_valid(green_percentage, vas_code):
    search = {}
    search['GreenPercentage'] = green_percentage
    search['VAS_Code'] = vas_code

    return search in vas_code_percentages


def is_green_percentage_vas_code_pair_valid(green_percentage, vas_code):
    valid = False

    if len(green_percentage) is 0 and len(vas_code) is 0:
        valid = True

    if len(green_percentage) is not 0 and len(vas_code) is not 0:
        valid = True

    return valid


def is_merchandise_merchandise_slug_merchandise_vesting_valid(merchandise, merchandise_slug, merchandise_vesting):
    valid = False

    if len(merchandise) is 0 and len(merchandise_slug) is 0 and len(merchandise_vesting) is 0:
        valid = True

    if len(merchandise) is not 0 and len(merchandise_slug) is not 0 and len(merchandise_vesting) is not 0:
        valid = True

    return valid


def is_ongoing_frequency_ongoing_value_valid(ongoing_frequency, ongoing_value):
    valid = False

    if len(ongoing_frequency) is 0 and len(ongoing_value) is 0:
        valid = True

    if len(ongoing_frequency) is not 0 and len(ongoing_value) is not 0:
        valid = True

    return valid


def is_partner_code_promo_code_valid(partner_code, promo_code):
    logger.debug('product_validate_multiple_fields.is_partner_code_promo_code_valid(): start.')

    search = {}
    search['PartnerCode'] = partner_code.lower()
    search['PromoCode'] = promo_code.lower()

    return search in partner_promotion_codes


def is_signup_bonus_signup_vesting_valid(signup_bonus, signup_vesting):
    valid = False

    if len(signup_bonus) is 0 and len(signup_vesting) is 0:
        valid = True

    if len(signup_bonus) is not 0 and len(signup_vesting) is not 0:
        valid = True

    return valid

