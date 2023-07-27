class TerminalColors:
    ''' Colors class for chart output. '''
    RED = '\033[31m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'


class Report:
    ''' Generates requested reports and shows them on the terminal.'''
    
    def year_report(readings):
        '''Prints year's report on terminal.'''
        print("---- YEAR REPORT ----")
        print('Highest: ', readings.highest, 'C on ',
              readings.highest_day, readings.highest_month)
        print("Lowest: ", readings.lowest,  'C on ',
              readings.lowest_day, readings.lowest_month)
        print("Humidity: ", readings.humidity, '% on ',
              readings.humid_day, readings.humid_month)

    def month_report(readings):
        '''Prints montht's report on terminal.'''
        print("----- MONTH REPORT ----")
        print('Highets Average: ', readings.highest_avg, 'C')
        print('Lowest Average: ', readings.lowest_avg, 'C')
        print('Average Mean Humidity: ', readings.humid_avg, '%')

    def month_chart(weather_readings):
        '''Prints line by line chart on terminal.'''

        for i in range(len(weather_readings)):
            date = (weather_readings[i].day).split('-')
            day = date[2]
            max_temp = weather_readings[i].max_temp

            if max_temp != '':
                print(TerminalColors.WHITE, "Day:", day, end="")
                for j in range(max_temp):
                    print(TerminalColors.RED + '+' + TerminalColors.RED, end="")
                print(TerminalColors.WHITE, "Temp:", max_temp, 'C')

            min_temp = weather_readings[i].min_temp

            if min_temp != '':
                print(TerminalColors.WHITE, "Day:", day, end="")
                for j in range(min_temp):
                    print(TerminalColors.BLUE + '+' + TerminalColors.BLUE, end="")
                print(TerminalColors.WHITE, " Temp:", min_temp, 'C', '\n')

    def month_chart_horizonral(weather_readings):
        '''Prints horizontal chart on terminal.'''

        for i in range(len(weather_readings)):
            date = (weather_readings[i].day).split('-')
            day = date[2]
            min_temp = weather_readings[i].min_temp

            if min_temp != '':
                print(TerminalColors.WHITE, "Day:", day, " ", end="")
                for j in range(min_temp):
                    print(TerminalColors.BLUE + '+' + TerminalColors.BLUE, end="")

            max_temp = weather_readings[i].max_temp

            if max_temp != '':
                for j in range(max_temp):
                    print(TerminalColors.RED + '+' + TerminalColors.RED, end="")
                print(TerminalColors.WHITE, " ", min_temp, 'C -', max_temp, 'C')


class Results:
    '''Data structure to hold result values.'''

    def year_results(self, highest, lowest, humid):
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
        self.highest_avg = highest_avg
        self.lowest_avg = lowest_avg
        self.humid_avg = humid_avg
