from flask import Blueprint
from controllers.weather import login, signup, home, year
from controllers.weather import month, charts, horizontal_chart, vertical_chart

reading_blueprint = Blueprint('reading_blueprint', __name__)

reading_blueprint.route('/home/', methods=['GET'])(home)
reading_blueprint.route('/signup/', methods=['GET', 'POST'])(signup)
reading_blueprint.route('/login/', methods=['GET', 'POST'])(login)
reading_blueprint.route('/year/', methods=['GET', 'POST'])(year)
reading_blueprint.route('/month/', methods=['GET', 'POST'])(month)
reading_blueprint.route('/charts/', methods=['GET'])(charts)
reading_blueprint.route('/charts/horizontal-chart/',
                        methods=['GET', 'POST'])(horizontal_chart)
reading_blueprint.route('/charts/vertical-chart/',
                        methods=['GET', 'POST'])(vertical_chart)
