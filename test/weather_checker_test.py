import unittest


class Weather:
    @classmethod
    def get(cls, city):
        return True


class MyTestCase(unittest.TestCase):
    def test_should_get_weather(self):
        forecast = Weather.get('Elizabeth, CO')
        self.assertIsNotNone(forecast)


if __name__ == '__main__':
    unittest.main()
