import json
from flask import Flask, render_template, redirect, url_for, request
from helpers.weatherman import *
from helpers.calculations import *
from helpers.report import *
from controllers.weather import *


def home():
    '''Renders home page. '''
    return render_template('home.html')


def signup():
    '''Renders signup page, asks for user details and 
        writes them in a file.'''
    if request.method == 'GET':
        return render_template('signup.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    with open("models/users.txt", "a") as fo:
        if (username and password):
            fo.write(username + ',' + password + "\n")
    return redirect(url_for('reading_bp.login'))


def login():
    '''Renders login page, takes user details and logs 
        them in if correct credentials given. '''
    if request.method == 'GET':
        return render_template('login.html')
    
    error = None
    req_username = request.form.get('username')
    req_password = request.form.get('password')
    
    with open('models/users.txt', 'r') as file:
        file_content = file.readlines()
        file_size = len(file_content)
        users = []
        for i in range(file_size):
            users.append(file_content[i])

    for i in range(len(users)):
        user = users[i]
        user = user.split(',')
        username = user[0]
        password = user[1].replace('\n', '')

        if (req_username == username and req_password == password):
            return redirect(url_for('reading_bp.home'))
    
    error = "Incorrect username or pasword."

    return render_template('login.html', error=error)


def year():
    '''Asks for year and redirects to that year's report.'''
    if request.method == "GET":
        return render_template('year.html')
    year = request.form.get("year")
    file_name = "weatherfiles/Murree_weather_" + year
    parse = ParsingData()
    weather_readings = parse.year_parsing(file_name)
    calculations = ReportCalculations()
    highest, lowest, humid = calculations.year_calculations(weather_readings)
    results = Results()
    results.year_results(highest, lowest, humid)
    return render_template("year_result.html", data=results)


def month():
    '''Asks for year and month, and redirects to that month's report.'''
    
    if request.method == 'GET':
        return render_template('month.html')
    year = request.form.get("year")
    month = request.form.get("month")
    file_name = ("weatherfiles/Murree_weather_" + year + "_" 
                                        + month + ".txt")
    parse = ParsingData()
    weather_readings = parse.month_parsing(file_name)
    highest_avg, lowest_avg, humid_avg = ReportCalculations.month_calculations(weather_readings)
    results = Results()
    results.month_results(highest_avg, lowest_avg, humid_avg)
    return render_template("month_result.html", data=results)


def chart():
    '''Renders charts page.'''
    return render_template('charts.html')


def h_chart():
    '''Renders horizontal chart page.'''
    year = request.form.get("year")
    month = request.form.get("month")
    file_name = ("weatherfiles/Murree_weather_" + year + "_"
                    + month + ".txt")
    parse = ParsingData()
    weather_readings = parse.month_parsing(file_name)
    return render_template("horizontal_chart.html", data=weather_readings)


def v_chart():
    '''Renders vertical chart page.'''
    year = request.form.get("year")
    month = request.form.get("month")
    file_name = ("weatherfiles/Murree_weather_" + year + "_"
                    + month + ".txt")
    parse = ParsingData()
    weather_readings = parse.month_parsing(file_name)
    return render_template("v_chart.html", data=weather_readings)

