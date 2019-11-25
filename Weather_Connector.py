import requests
import json

# class to build weather api connector
class Weather(object):

    def __init__(self):
        self.city = "Beaver Falls, PA"
        self.key = "c0c568d77269893bb1e7ff39b88e707d"

    def get_forcast(self):

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(self.city, self.key)
        two_weeks_forecast = requests.get(url).json()
        print(two_weeks_forecast)


loc_weather = Weather()

loc_weather.get_forcast()
