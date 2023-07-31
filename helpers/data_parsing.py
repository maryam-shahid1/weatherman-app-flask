from helpers.weather_reading import WeatherReading
from helpers.weatherman import get_month
import os

  
class ParsingData:
    '''Reads data from files and parses it'''

    def parsing_file_data(self, file):
        file_content = file.readlines()
        file_size = len(file_content)
        readings_list = []

        for i in range(1, file_size):
            data = file_content[i]
            data = data.split(',')
            
            reading = {
                "day":  data[0],
                "humidity": data[8],
                "mean_temp": data[2],
                "lowest_temp": data[3],
                "highest_temp": data[1]
                }
            
            day = reading.get("day", None)
            max_temp = mean_temp = min_temp = mean_humidity = ''
            if reading["highest_temp"] and reading["highest_temp"] != ',':
                max_temp = int(reading["highest_temp"])
            if reading["mean_temp"] and reading["mean_temp"] != ',':
                mean_temp = int(reading["mean_temp"])
            if reading["lowest_temp"] and reading["lowest_temp"] != ',':
                min_temp = int(reading["lowest_temp"])
            if reading["humidity"] and reading["humidity"] != ',':
                mean_humidity = int(reading["humidity"])

            readings_list.append(WeatherReading(day, max_temp, mean_temp, 
                                                min_temp, mean_humidity))
        return readings_list

    def month_parsing(self, file_name):
        '''Parses data according to month report requirements.'''
        with open(file_name, "r") as file:
            file = open(file_name, "r")
            list = self.parsing_file_data(file)
        return list

    def year_parsing(self, filename):
        '''Parses data according to year report requirements.'''
        monthly_readings = []
        for i in range(1, 12):
            file_name = f'{filename}_{get_month(i)}.txt'
            if os.path.isfile(file_name):
                file = open(file_name)
                list = self.parsing_file_data(file)
                monthly_readings.append(list)
        return monthly_readings
