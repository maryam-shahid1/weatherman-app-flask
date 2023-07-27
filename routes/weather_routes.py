from flask import Blueprint
from controllers.weather import home, signup, login, year, month, chart, h_chart, v_chart

reading_bp = Blueprint('reading_bp', __name__)

reading_bp.route('/', methods=['GET'])(home)
reading_bp.route('/signup/', methods=['GET', 'POST'])(signup)
reading_bp.route('/login/', methods=['GET', 'POST'])(login)
reading_bp.route('/year/', methods=['GET', 'POST'])(year)
reading_bp.route('/month/', methods=['GET', 'POST'])(month)
reading_bp.route('/chart', methods=['GET'])(chart)
reading_bp.route('/chart/horizontal_chart', methods=['GET', 'POST'])(h_chart)
reading_bp.route('/chart/vertical_chart', methods=['GET', 'POST'])(v_chart)

