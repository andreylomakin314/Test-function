import unittest

from city_description_function import get_population_city_country


class NameTestCase(unittest.TestCase):
    """Тестирует функцию по заданным значениям"""
    def test(self):
        """Тестирует со значениями город и страна"""
        message = get_population_city_country('penza', 'russia')
        self.assertEqual(message, 'Penza Russia')

    def test_all_values(self):
        """Тестирует со значениями горд, страна и население"""
        message = get_population_city_country(
            'pattaya', 'thailand', 'population=2000000')
        self.assertEqual(message, 'Pattaya Thailand Population=2000000')


unittest.main()
