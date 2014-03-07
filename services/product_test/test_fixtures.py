__author__ = 'breichard'


test_cases_proto = [ dict(
                    products = [{"BrandSlug": "energyplus", "Channel": "web"}, {"BrandSlug": "nrg_residential", "Channel": "Retention"}],
                    expected = [{"BrandSlug": "energyplus", "Channel": "web", "Errors": {}}, {"BrandSlug": "nrg_residential", "Channel": "Retention", "Errors": {}}]
                ),
               dict(
                    products = [{"BrandSlug": "energyplus", "Channel": "web"}, {"BrandSlug": "nrg_residential", "Channel": "Retention"}],
                    expected = [{"BrandSlug": "energyplus", "Channel": "web", "Errors": {}}, {"BrandSlug": "nrg_residential", "Channel": "Retention", "Errors": {}}]
                ),
                dict(
                    products = [{"BrandSlug": "energyplus", "Channel": "web"}, {"BrandSlug": "nrg_residential", "Channel": "Retention"}],
                    expected = [{"BrandSlug": "energyplus", "Channel": "web", "Errors": {}}, {"BrandSlug": "nrg_residential", "Channel": "Retention", "Errors": {}}]
                ),
                dict(
                    products = [{"BrandSlug": "energyplus", "Channel": "web"}, {"BrandSlug": "nrg_residential", "Channel": "Retention"}],
                    expected = [{"BrandSlug": "energyplus", "Channel": "web", "Errors": {}}, {"BrandSlug": "nrg_residential", "Channel": "Retention", "Errors": {}}]
                )]


test_cases = test_cases_proto + test_cases_proto