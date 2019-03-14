# app.py
from flask import Flask
from flask_restplus import Resource, Api, fields
from flask.json import jsonify
from flask import request
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
from apis import api

application = Flask(__name__)
CORS(application)
application.wsgi_app = ProxyFix(application.wsgi_app)
api.init_app(application)

if __name__ == '__main__':
    application.run(debug=True)