from flask import Blueprint

home = Blueprint('home', __name__)


@home.route('/api/datasource/list', methods=['GET'])
def index():
    return {
        'data': 'Hello World!',
    }, 200
