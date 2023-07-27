def get_month(value):
    ''' Returns month corresponding to the given nmerical value.'''
    months = {
                1: 'Jan', 2: 'Feb', 3: 'Mar',
                4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep',
                10: 'Oct', 11: 'Nov', 12: 'Dec'
            }
    return months[value]


def get_values(day, month, temp):
    '''Compacts the readings into a single dictionary for better access.'''
    values = {"day": day, "month": month, "temp": temp}
    return values


def get_day_and_month(date):
    ''' Extracts day and month from a date.'''
    data = date.split('-')
    date = {
        "day": data[2],
        "month": get_month(int(data[1]))
    }
    return date["day"], date["month"]


class ReportCalculations:

    '''A class that calculates monthly and yearly weather report statistics.'''

    def month_calculations(weather_readings):
        '''Calculates average highest temperature, average lowest
            temperature, and average humidity for a month.'''

        max_count = 0
        min_count = 0
        humidity_count = 0
        max_temp_sum = 0
        min_temp_sum = 0
        humidity_sum = 0

        for i in range(len(weather_readings)):

            if weather_readings[i].max_temp != '':
                max_temp_sum += weather_readings[i].max_temp
                max_count += 1
            if weather_readings[i].min_temp != '':
                min_temp_sum += weather_readings[i].min_temp
                min_count += 1
            if weather_readings[i].mean_humidity != '':
                humidity_sum += weather_readings[i].mean_humidity
                humidity_count += 1

        avg_highest = round(max_temp_sum / max_count)
        avg_lowest = round(min_temp_sum / min_count)
        avg_humidity = round(humidity_sum / humidity_count)

        return avg_highest, avg_lowest, avg_humidity

    def year_calculations(self, weather_readings):
        '''Calculates highest temperature, lowest temperature, 
            and highest humidity for the year.'''
        highest_temp = -100
        highest_temp_day = ''
        lowest_temp = 100
        lowest_temp_day = ''
        most_humid = 0
        most_humid_day = ''

        for i in range(len(weather_readings)):
            for reading in weather_readings[i]:

                if (reading.max_temp != '' and
                        reading.max_temp > highest_temp):
                    highest_temp = reading.max_temp
                    highest_temp_day = reading.day

                if (reading.min_temp != '' and
                        reading.min_temp < lowest_temp):
                    lowest_temp = reading.min_temp
                    lowest_temp_day = reading.day

                if (reading.mean_humidity != '' and
                        reading.mean_humidity > most_humid):
                    most_humid = reading.mean_humidity
                    most_humid_day = reading.day

        highest_day, highest_month = get_day_and_month(highest_temp_day)
        lowest_day, lowest_month = get_day_and_month(lowest_temp_day)
        humid_day, humid_month = get_day_and_month(most_humid_day)

        highest_values = get_values(highest_day, highest_month,
                                       highest_temp)
        lowest_values = get_values(lowest_day, lowest_month,
                                      lowest_temp)
        humid_values = get_values(humid_day, humid_month,
                                     most_humid)

        return highest_values, lowest_values, humid_values
