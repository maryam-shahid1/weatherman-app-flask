''' This module consists of class DataParser that reads weather readings
from files and parses them which is used to generate reports.'''
import os

from helpers.weather_reading import WeatherReading
from helpers.calculations import get_month


class DataParser:
    '''Reads data from files and parses it'''

    def parsing_file_data(self, file):
        file_content = file.readlines()
        file_size = len(file_content)
        readings_list = []

        for i in range(1, file_size):
            data = file_content[i]
            data = data.split(',')

            reading = {
                "day": data[0],
                "highest_temp": data[1],
                "mean_temp": data[2],
                "lowest_temp": data[3],
                "humidity": data[8]
                }

            day = reading["day"]
            max_temp = mean_temp = min_temp = mean_humidity = ""
            if reading["highest_temp"] and reading["highest_temp"] != ",":
                max_temp = int(reading["highest_temp"])
            if reading["mean_temp"] and reading["mean_temp"] != ",":
                mean_temp = int(reading["mean_temp"])
            if reading["lowest_temp"] and reading["lowest_temp"] != ",":
                min_temp = int(reading["lowest_temp"])
            if reading["humidity"] and reading["humidity"] != ",":
                mean_humidity = int(reading["humidity"])

            readings_list.append(WeatherReading(day, max_temp, mean_temp,
                                                min_temp, mean_humidity))
        return readings_list

    def month_parsing(self, file_name): 
        '''Parses data according to month report requirements.'''
        with open(file_name, "r", encoding="utf-8") as file:
            month_list = self.parsing_file_data(file)
        return month_list

    def year_parsing(self, filename):
        '''Parses data according to year report requirements.'''
        monthly_readings = []
        for i in range(1, 12):
            file_name = f'{filename}_{get_month(i)}.txt'
            if os.path.isfile(file_name):
                with open(file_name, "r", encoding="utf-8") as file:
                    readings = self.parsing_file_data(file)
                monthly_readings.append(readings)
        return monthly_readings
