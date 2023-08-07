"""
Module containing the WeatherReading class for representing weather data.
"""


class WeatherReading:
    '''Represents a weather reading with temperature and humidity data.'''
    def __init__(self, day, max_temp, mean_temp,
                 min_temp, mean_humidity):
        self.day = day
        self.max_temp = max_temp
        self.mean_temp = mean_temp
        self.min_temp = min_temp
        self.mean_humidity = mean_humidity
