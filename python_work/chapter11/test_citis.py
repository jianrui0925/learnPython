import unittest
from city_functions import *

class CityTestCase(unittest.TestCase):
    """测试city_functions.py"""
    def test_city_function(self):
        country_city = city_function('China','xiangtan')
        self.assertEqual(country_city,'China , Xiangtan')
    
    def test_city_country_population(self):
        str = city_function('china','xiangtan','5000000')
        self.assertEqual(str,'China , Xiangtan , Population 5000000')

if __name__ =='__main__':
    unittest.main()