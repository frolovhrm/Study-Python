import unittest
from exercise11_01 import city_country


class CitesTest(unittest.TestCase):
    """Тест для упражнения 11_01"""
    def test_city_country(self):
        """Собирается ли пара 'Город, Страна'? """
        c_c = city_country('santiago', 'chile')
        self.assertEqual(c_c, 'Santiago, Chile')

    def test_city_country_population(self):
        """Собирается ли пара 'Город, Страна - население'? """
        c_c_p = city_country('santiago', 'chile', 5000000)
        self.assertEqual(c_c_p, 'Santiago, Chile - Population 5000000')
