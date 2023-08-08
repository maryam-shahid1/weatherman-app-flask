from flask import Flask, render_template, redirect, url_for, request
from helpers.weatherman import *
from helpers.calculations import *
from helpers.report import *
from controllers.weather import *


def index():
    return render_template('home.html')


def year():
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
    return render_template('charts.html')


def h_chart():
    year = request.form.get("year")
    month = request.form.get("month")
    file_name = ("weatherfiles/Murree_weather_" + year + "_"
                    + month + ".txt")

    parse = ParsingData()

    weather_readings = parse.month_parsing(file_name)

    return render_template("horizontal_chart.html", data=weather_readings)


def v_chart():
    year = request.form.get("year")
    month = request.form.get("month")
    file_name = ("weatherfiles/Murree_weather_" + year + "_"
                    + month + ".txt")

    parse = ParsingData()

    weather_readings = parse.month_parsing(file_name)

    return render_template("v_chart.html", data=weather_readings)


