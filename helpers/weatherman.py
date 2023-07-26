import sys
import os
from helpers.calculations import *


def months_list():
    return ['Jan', 'Feb', 'Mar',
            'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep',
            'Oct', 'Nov', 'Dec']


class WeatherReading:

    def __init__(self, day, max_temp, mean_temp,
                 min_temp, mean_humidity):
        self.day = day
        self.max_temp = max_temp
        self.mean_temp = mean_temp
        self.min_temp = min_temp
        self.mean_humidity = mean_humidity


class ParsingData:

    def parsing_data(self, file):
        file_content = file.readlines()
        file_size = len(file_content)
        list = []

        for i in range(1, file_size):
            data = file_content[i]
            reading = data.split(',')
            day = reading[0]
            max_temp = mean_temp = min_temp = mean_humidity = ''
            if reading[1] != '' and reading[1] != ',':
                max_temp = int(reading[1])
            if reading[2] != '' and reading[2] != ',':
                mean_temp = int(reading[2])
            if reading[3] != '' and reading[3] != ',':
                min_temp = int(reading[3])
            if reading[8] != '' and reading[8] != ',':
                mean_humidity = int(reading[8])

            list.append(WeatherReading(day, max_temp, mean_temp,
                                       min_temp, mean_humidity))
        return list

    def month_parsing(self, file_name):
        file = open(file_name, "r")
        list = self.parsing_data(file)
        return list

    def year_parsing(self, filename):
        monthly_readings = []
        months = months_list()
        for i in range(12):
            file_name = filename + '_' + months[i] + '.txt'
            if os.path.isfile(file_name):
                file = open(file_name)
                list = self.parsing_data(file)
                monthly_readings.append(list)
        return monthly_readings


# def main():

    
#     arguments_len = len(sys.argv)
#     type_index = 1

#     for i in range(2, arguments_len, 2):
#         report_type = sys.argv[type_index]

#         if (report_type == '-e'):
#             year = sys.argv[i]
#             file_name = "weatherfiles/Murree_weather_" + year

#             parse = ParsingData()
#             weather_readings = parse.year_parsing(file_name)

#             calculations = ReportCalculations()
#             highest, lowest, humid = calculations.year_calculations(weather_readings)

#             results = Results()
#             results.year_results(highest, lowest, humid)
            
#             Report.year_report(results)
#             print('\n')

#         elif report_type == '-a':
#             period = sys.argv[i]
#             data = period.split('/')
#             year = data[0]
#             month = int(data[1])
#             month_list = months_list()
#             file_name = ("weatherfiles/Murree_weather_" + year + "_"
#                          + month_list[month-1] + ".txt")

#             parse = ParsingData()
#             weather_readings = parse.month_parsing(file_name)

#             highest_avg, lowest_avg, humid_avg = ReportCalculations.month_calculations(weather_readings)

#             results = Results()
#             results.month_results(highest_avg, lowest_avg, humid_avg)

#             Report.month_report(results)
#             print('\n')

#         elif report_type == '-c':
#             period = sys.argv[i]
#             data = period.split('/')
#             year = data[0]
#             month = int(data[1])
#             month_list = months_list()
#             file_name = ("weatherfiles/Murree_weather_" + year + "_"
#                          + month_list[month-1] + ".txt")

#             parse = ParsingData()
#             weather_readings = parse.month_parsing(file_name)

#             Report.month_chart(weather_readings)
#             print('---- Horizontal Chart ----')
#             Report.month_chart_horizonral(weather_readings)

#         type_index = type_index + 2


if __name__ == '__main__':
    main()
