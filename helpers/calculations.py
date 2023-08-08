"""
This module contains utility functions and classes for calculating
weather report statistics.

It provides functions to convert numerical months to their
corresponding abbreviations, compact weather readings into a
single dictionary for better access, and extract day and month
from a given date. Additionally, it includes the ReportCalculator class,
which calculates various weather report statistics such as average
temperatures, highest and lowest temperatures, and highest humidity for
both monthly and yearly periods.

"""


def get_month(month):
    '''Returns the month corresponding to the given numerical value.'''
    months_list = {
        1: 'Jan', 2: 'Feb', 3: 'Mar',
        4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep',
        10: 'Oct', 11: 'Nov', 12: 'Dec'
    }
    return months_list[month]


def get_day_month_and_temp_values(day, month, temp):
    '''Compacts the readings into a single dictionary for better access.'''
    return {"day": day, "month": month, "temp": temp}


def get_day_and_month(date):
    '''Extracts day and month from the given date.'''
    data = date.split('-')
    return data[2], get_month(int(data[1]))


class ReportCalculator:
    '''A class that calculates monthly and yearly weather report statistics.'''

    def calculate_highest_values(self, weather_readings, is_max):
        '''Calculates the highest values (temperature or humidity)
            and corresponding days.'''
        value, day = -100.0, ''
        for weather in weather_readings:
            for reading in weather:
                if is_max:
                    if reading.max_temp and reading.max_temp > value:
                        value = reading.max_temp
                        day = reading.day
                else:
                    if reading.mean_humidity and reading.mean_humidity > value:
                        value = reading.mean_humidity
                        day = reading.day

        return value, day

    def calculate_lowest_values(self, weather_readings):
        '''Calculates the lowest temperature value and corresponding day.'''
        value, day = 100.0, ''
        for weather in weather_readings:
            for reading in weather:
                if reading.min_temp and reading.min_temp < value:
                    value = reading.max_temp
                    day = reading.day

        return value, day

    def month_calculations(self, weather_readings):
        '''Calculates average highest temperature, average lowest temperature,
        and average humidity for a month.'''
        max_count = min_count = humidity_count = 0
        max_temp_sum = min_temp_sum = humidity_sum = 0

        for weather in weather_readings:
            if weather.max_temp:
                max_temp_sum += weather.max_temp
                max_count += 1
            if weather.min_temp:
                min_temp_sum += weather.min_temp
                min_count += 1
            if weather.mean_humidity:
                humidity_sum += weather.mean_humidity
                humidity_count += 1

        avg_highest = round(max_temp_sum / max_count)
        avg_lowest = round(min_temp_sum / min_count)
        avg_humidity = round(humidity_sum / humidity_count)

        return avg_highest, avg_lowest, avg_humidity

    def year_calculations(self, weather_readings):
        '''Calculates highest temperature, lowest temperature,
        and highest humidity for the year.'''
        highest_temp = -100.0
        lowest_temp = 100.0
        most_humid = 0.0
        highest_temp_day = lowest_temp_day = most_humid_day = ''

        highest_temp, highest_temp_day = self.calculate_highest_values(
            weather_readings,
            is_max=True)
        lowest_temp, lowest_temp_day = self.calculate_lowest_values(
            weather_readings)
        most_humid, most_humid_day = self.calculate_highest_values(
            weather_readings,
            is_max=False)

        for weather in weather_readings:
            for reading in weather:
                if reading.max_temp and reading.max_temp > highest_temp:
                    highest_temp = reading.max_temp
                    highest_temp_day = reading.day

                if reading.min_temp and reading.min_temp < lowest_temp:
                    lowest_temp = reading.min_temp
                    lowest_temp_day = reading.day

                if reading.mean_humidity and \
                        reading.mean_humidity > most_humid:
                    most_humid = reading.mean_humidity
                    most_humid_day = reading.day

        highest_temp_day, highest_temp_month = get_day_and_month(
            highest_temp_day
            )
        lowest_temp_day, lowest_temp_month = get_day_and_month(lowest_temp_day)
        humid_day, humid_month = get_day_and_month(most_humid_day)

        highest_values = get_day_month_and_temp_values(
            highest_temp_day,
            highest_temp_month,
            highest_temp
        )
        lowest_values = get_day_month_and_temp_values(
            lowest_temp_day,
            lowest_temp_month,
            lowest_temp
        )
        humid_values = get_day_month_and_temp_values(
            humid_day,
            humid_month,
            most_humid
        )

        return highest_values, lowest_values, humid_values
