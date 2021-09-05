import unittest
from datetime import datetime,timedelta
from geopy.geocoders import Nominatim


class Weather:
    @classmethod
    def get(cls, lat, lon):
        # now = datetime.now()
        # start = now + timedelta(days=-1)
        # d_from_date = datetime.strptime(start.strftime('%Y-%m-%d'), '%Y-%m-%d')
        # new_date = (d_from_date + timedelta(days=i)).strftime('%Y-%m-%d')
        # search_date = new_date+"T00:00:00"
        # response = requests.get("https://api.darksky.net/forecast/"+cfg.DARK_SKY_API_KEY+"/"+latitude+","+longitude+","+search_date+"?"+option_list)
        # return response
        pass

class Utilities:
    def geocode(city):
        geolocator = Nominatim(user_agent="my-weather-app")
        return geolocator.geocode(city)



class MyTestCase(unittest.TestCase):
    def test_should_get_location(self):
        location = Utilities.geocode("Elizabeth, CO")
        self.assertEqual(location.latitude, 10.7244991)
        self.assertEqual(location.longitude, -73.0962968)

    # def test_should_get_weather(self):
    #     forecast = Weather.get(lat, lon)
    #     self.assertIsNotNone(forecast)


if __name__ == '__main__':
    unittest.main()
