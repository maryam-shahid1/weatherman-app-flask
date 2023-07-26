class bcolors:
    RED = '\033[31m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'


class Report:

    def year_report(values):
        print("---- YEAR REPORT ----")
        print('Highest: ', values.highest, 'C on ',
              values.highest_day, values.highest_month)
        print("Lowest: ", values.lowest,  'C on ',
              values.lowest_day, values.lowest_month)
        print("Humidity: ", values.humidity, '% on ',
              values.humid_day, values.humid_month)

    def month_report(values):
        print("----- MONTH REPORT ----")
        print('Highets Average: ', values.highest_avg, 'C')
        print('Lowest Average: ', values.lowest_avg, 'C')
        print('Average Mean Humidity: ', values.humid_avg, '%')

    def month_chart(weather_readings):

        for i in range(len(weather_readings)):
            date = (weather_readings[i].day).split('-')
            day = date[2]
            max_temp = weather_readings[i].max_temp

            if max_temp != '':
                print(bcolors.WHITE, "Day:", day, end="")
                for j in range(max_temp):
                    print(bcolors.RED + '+' + bcolors.RED, end="")
                print(bcolors.WHITE, "Temp:", max_temp, 'C')

            min_temp = weather_readings[i].min_temp

            if min_temp != '':
                print(bcolors.WHITE, "Day:", day, end="")
                for j in range(min_temp):
                    print(bcolors.BLUE + '+' + bcolors.BLUE, end="")
                print(bcolors.WHITE, " Temp:", min_temp, 'C', '\n')

    def month_chart_horizonral(weather_readings):

        for i in range(len(weather_readings)):
            date = (weather_readings[i].day).split('-')
            day = date[2]
            min_temp = weather_readings[i].min_temp

            if min_temp != '':
                print(bcolors.WHITE, "Day:", day, " ", end="")
                for j in range(min_temp):
                    print(bcolors.BLUE + '+' + bcolors.BLUE, end="")

            max_temp = weather_readings[i].max_temp

            if max_temp != '':
                for j in range(max_temp):
                    print(bcolors.RED + '+' + bcolors.RED, end="")
                print(bcolors.WHITE, " ", min_temp, 'C -', max_temp, 'C')


class Results:

    def year_results(self, highest, lowest, humid):
        self.highest_day = highest[0]
        self.highest_month = highest[1]
        self.highest = highest[2]

        self.lowest_day = lowest[0]
        self.lowest_month = lowest[1]
        self.lowest = lowest[2]

        self.humid_day = humid[0]
        self.humid_month = humid[1]
        self.humidity = humid[2]

    def month_results(self, highest_avg, lowest_avg, humid_avg):
        self.highest_avg = highest_avg
        self.lowest_avg = lowest_avg
        self.humid_avg = humid_avg
