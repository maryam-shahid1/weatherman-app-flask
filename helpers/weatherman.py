import sys
import os
from helpers.calculations import *
from helpers.weather_reading import *
from helpers.data_parsing import *
from helpers.report import *


def get_month(value):
    ''' Returns month name corresponding to the given numerical value'''
    months = {
                1: 'Jan', 2: 'Feb', 3: 'Mar',
                4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep',
                10: 'Oct', 11: 'Nov', 12: 'Dec'
            }
    return months[value]


def main():

    arguments_len = len(sys.argv)
    type_index = 1

    for i in range(2, arguments_len, 2):
        report_type = sys.argv[type_index]

        if (report_type == '-e'):
            '''Handling request for year's report'''
            year = sys.argv[i]
            year_value = int(year)

            if (year_value < 2004 or year_value > 2016):
                print("Year out of range!")
                break 

            file_name = "weatherfiles/Murree_weather_" + year

            parse = ParsingData()
            weather_readings = parse.year_parsing(file_name)

            calculations = ReportCalculations()
            highest, lowest, humid = calculations.year_calculations(weather_readings)

            results = Results()
            results.year_results(highest, lowest, humid)
            
            Report.year_report(results)
            print('\n')

        elif report_type == '-a':
            '''Handling request for month's report'''
            period = sys.argv[i]
            data = period.split('/')
            year = data[0]
            year_value = int(year)
            month = int(data[1])
            
            if (year_value < 2004 or year_value > 2016):
                print("Year out of range!")
                break

            if (month < 1 or month > 12):
                print("Month out of range!")
                break

            month = get_month(month)

            file_name = ("weatherfiles/Murree_weather_" + year + "_"
                         + month + ".txt")

            parse = ParsingData()
            weather_readings = parse.month_parsing(file_name)

            highest_avg, lowest_avg, humid_avg = ReportCalculations.month_calculations(weather_readings)

            results = Results()
            results.month_results(highest_avg, lowest_avg, humid_avg)

            Report.month_report(results)
            print('\n')

        elif report_type == '-c':
            '''Handling request for month's charts'''
            period = sys.argv[i]
            data = period.split('/')
            year = data[0]
            year_value = int(year)
            month = int(data[1])

            if (year_value < 2004 or year_value > 2016):
                print("Year out of range!")
                break

            if (month < 1 or month > 12):
                print("Month out of range!")
                break

            month = get_month(month)
            file_name = ("weatherfiles/Murree_weather_" + year + "_"
                         + month + ".txt")

            parse = ParsingData()
            weather_readings = parse.month_parsing(file_name)

            Report.month_chart(weather_readings)
            print('---- Horizontal Chart ----')
            Report.month_chart_horizonral(weather_readings)

        type_index = type_index + 2


if __name__ == '__main__':
    main()
