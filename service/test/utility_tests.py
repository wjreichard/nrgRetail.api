import unittest
from service import utility


class TestValidateUtility(unittest.TestCase):

    def test_csv_bytes_to_json(self):

        csv_bytes = '"BrandSlug","Channel"\n"energyplus","web"'.encode('utf-8')
        expected_result = '[{"BrandSlug": "energyplus", "Channel": "web"}]'

        result = utility.csv_bytes_to_json(csv_bytes)

        self.assertEqual(result, expected_result)

    def test_dict_to_csv(self):

        dictionary = [{"BrandSlug": "energyplus", "Channel": "web"}]
        expected_result = '"BrandSlug","Channel"\n"energyplus","web"\n'

        result = utility.dict_to_csv(dictionary)

        self.assertEqual(result, expected_result)


    def test_sku_generator(self):

        result = utility.sku_generator()
        self.assertEqual(len(result), 13)


if __name__ == '__main__':
    unittest.main()


