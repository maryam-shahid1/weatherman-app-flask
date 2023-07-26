def months_list():
    return ['Jan', 'Feb', 'Mar',
            'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep',
            'Oct', 'Nov', 'Dec']


def append_values(day, month, temp):
    values = []
    values.append(day)
    values.append(month)
    values.append(temp)
    return values


def dayAndMonth(date):
    data = date.split('-')
    day = data[2]
    month = data[1]
    month_list = months_list()
    month = month_list[int(month)-1]
    return day, month


class ReportCalculations:

    def month_calculations(weather_readings):
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

        highest_day, highest_month = dayAndMonth(highest_temp_day)
        lowest_day, lowest_month = dayAndMonth(lowest_temp_day)
        humid_day, humid_month = dayAndMonth(most_humid_day)

        highest_values = append_values(highest_day, highest_month,
                                       highest_temp)
        lowest_values = append_values(lowest_day, lowest_month,
                                      lowest_temp)
        humid_values = append_values(humid_day, humid_month,
                                     most_humid)

        return highest_values, lowest_values, humid_values
