from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

from src.models import User, Post, ViewHistory

"""
Application Simple 1
"""
def create_app():
    app = Flask(__name__)

    # load the instance config, if it exists, when not testing
    app.config.from_object('src.config.BaseConfiguration')

    cors = CORS(app, resources={r"*": {"origins": app.config['CORS']}})
     
    # All the posts are displayed
    # Start
    @app.route('/test/<input_valve>')
    def test_function(input_valve):
        result = 10 * input_valve
        return jsonify({'result': result})
    # End

    return app
    # End