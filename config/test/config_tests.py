__author__ = 'rike'

import unittest
from  config import config


class TestConfig(unittest.TestCase):

    def test_can_read_config_ini_file(self):

        result = config.enrollment_connection_string
        self.assertEqual('database=' in result.lower(), True)


if __name__ == '__main__':
    unittest.main()



