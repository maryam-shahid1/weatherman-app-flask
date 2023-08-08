"""
Module for generating weather reports and displaying them on the terminal.
"""


class Report:
    ''' Generates requested reports and shows them on the terminal.'''

    def month_temperature_stats(self, weather_readings):
        '''Prints line by line chart on terminal.'''
        month_temperature_stats = []
        for weather in weather_readings:
            date = (weather.day).split('-')
            day = date[2]
            if weather.max_temp:
                max_temp = weather.max_temp
            if weather.min_temp:
                min_temp = weather.min_temp
            day_temp_stats = {
                'date': day,
                'max_temp': max_temp,
                'min_temp': min_temp
                }
            month_temperature_stats.append(day_temp_stats)

        return month_temperature_stats


class Results:
    '''Data structure to hold result values.'''

    def year_results(self, highest, lowest, humid):
        '''Initializes attributes for year's report.'''
        self.highest_day = highest["day"]
        self.highest_month = highest["month"]
        self.highest = highest["temp"]

        self.lowest_day = lowest["day"]
        self.lowest_month = lowest["month"]
        self.lowest = lowest["temp"]

        self.humid_day = humid["day"]
        self.humid_month = humid["month"]
        self.humidity = humid["temp"]

    def month_results(self, highest_avg, lowest_avg, humid_avg):
        '''Initializes attributes for month's report.'''
        self.highest_avg = highest_avg
        self.lowest_avg = lowest_avg
        self.humid_avg = humid_avg
