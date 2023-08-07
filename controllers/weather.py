import hashlib
import os

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    abort,
    jsonify
)
from helpers.weather_reading import WeatherReading
from helpers.calculations import ReportCalculator
from helpers.report import Results, Report
from helpers.data_parsing import DataParser


USER_FILE = 'models/users.txt'
WEATHER_FILES_DIR = 'weatherfiles'


def home():
    '''Renders home page. '''
    return render_template('home.html')


def signup():
    """
    Sign up a new user.

    ### Example Request:
        POST /signup

    ### Example Response:
    {
        "response_code": 302,
        "response_message": "Redirecting to login page"
    }
    """
    if request.method == 'GET':
        return render_template('signup.html')

    try:
        username = request.form.get('username')
        password = request.form.get('password')

        if not (username and password):
            abort(401)

        hashed_password = str(
            hashlib.md5(password.encode()).hexdigest()
        )

        with open(USER_FILE, 'a', encoding='utf-8') as file:
            file.write(f'{username},{hashed_password}\n')

        return redirect(url_for('reading_blueprint.login'))

    except Exception as error:
        return jsonify(error=str(error)), 500


def login():
    """
    Log in a user.

    ### Example Request:
        POST /login

    ### Example Response:
    {
        "response_code": 302,
        "response_message": "Redirecting to home page"
    }
    """
    if request.method == 'GET':
        return render_template('login.html')

    try:
        req_username = request.form.get('username')
        req_password = request.form.get('password')
        req_password_hash = hashlib.md5(
            req_password.encode()
            ).hexdigest()

        with open(USER_FILE, 'r', encoding='utf-8') as file:
            users = file.readlines()

        for user in users:
            username, password = user.strip().split(',')
            if (req_username == username and
                    req_password_hash == password):
                return redirect(url_for('reading_blueprint.home'))

    except Exception as error:
        return jsonify(error=str(error)), 500


def year():
    """
    Get weather report for a specific year.

    ### Example Request:
        POST /year

    ### Example Response:
    {
        "response_code": 200,
        "response_message": "Yearly report generated",
        "data": {
            "highest_temperature": 30.5,
            "lowest_temperature": 10.2,
            "average_humidity": 68.7
        }
    }
    """
    if request.method == 'GET':
        return render_template('year.html')

    try:
        year = request.form.get("year")
        file_name = os.path.join(
            WEATHER_FILES_DIR,
            f'Murree_weather_{year}'
        )

        parse = DataParser()
        weather_readings = parse.year_parsing(file_name)

        calculations = ReportCalculator()
        highest, lowest, humid = calculations.year_calculations(
            weather_readings
        )

        results = Results()
        results.year_results(highest, lowest, humid)

        return render_template('year_result.html', data=results)

    except Exception as error:
        return jsonify(str(error)), 500


def month():
    """
    Get weather report for a specific month.

    ### Example Request:
        POST /month

    ### Example Response:
    {
        "response_code": 200,
        "response_message": "Monthly report generated",
        "data": {
            "average_highest_temperature": 25.6,
            "average_lowest_temperature": 14.3,
            "average_humidity": 72.4
        }
    }
    """
    if request.method == 'GET':
        return render_template('month.html')

    try:
        year = request.form.get('year')
        month = request.form.get('month')

        file_name = os.path.join(
            WEATHER_FILES_DIR,
            f'Murree_weather_{year}_{month}.txt'
        )
        parse = DataParser()

        weather_readings = parse.month_parsing(file_name)
        report = ReportCalculator()
        highest_avg, lowest_avg, humid_avg = report.month_calculations(
            weather_readings
            )

        results = Results()
        results.month_results(highest_avg, lowest_avg, humid_avg)

        return render_template('month_result.html', data=results)

    except Exception as error:
        return jsonify(str(error)), 500


def charts():
    '''Gets chart page.'''
    return render_template('charts.html')


def horizontal_chart():
    """
    Get horizontal chart page.

    ### Example Request:
        POST /horizontal_chart

    ### Example Response:
    {
        "response_code": 200,
        "response_message": "Horizontal chart page rendered"
    }
    """
    try:
        year = request.form.get('year')
        month = request.form.get('month')
        file_name = os.path.join(
            WEATHER_FILES_DIR,
            f'Murree_weather_{year}_{month}.txt'
        )

        parse = DataParser()
        weather_readings = parse.month_parsing(file_name)

        report = Report()
        month_stats = report.month_temperature_stats(weather_readings)

        return render_template('horizontal_chart.html', data=month_stats)

    except Exception as error:
        return jsonify(str(error)), 500


def vertical_chart():
    """
    Get vertical chart page.

    ### Example Request:
        POST /vertical_chart

    ### Example Response:
    {
        "response_code": 200,
        "response_message": "Vertical chart page rendered"
    }
    """

    try:
        year = request.form.get('year')
        month = request.form.get('month')

        file_name = os.path.join(
            WEATHER_FILES_DIR,
            f'Murree_weather_{year}_{month}.txt')
        parse = DataParser()

        weather_readings = parse.month_parsing(file_name)

        report = Report()
        month_stats = report.month_temperature_stats(weather_readings)

        return render_template('vertical_chart.html', data=month_stats)

    except Exception as error:
        return jsonify(str(error)), 500
