import requests
import os


class Weather(object):

    def __init__(self):
        self.api_key = "Some Key"

    def print_key(self):
        print(self.api_key)


loc_weather = Weather()
loc_weather.print_key()
