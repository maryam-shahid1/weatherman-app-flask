from flask import Flask, request, render_template, redirect, url_for
from routes.weather_routes import reading_bp

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(reading_bp, url_prefix='/weather')

@app.route('/')
def index():
    '''Renders home page. '''
    return render_template('home.html')

