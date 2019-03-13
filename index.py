# app.py
from flask import Flask
from flask_restplus import Resource, Api, fields
from flask.json import jsonify
from flask import request
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
from apis import api

app = Flask(__name__)
# CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
CORS(api.init_app(app))

if __name__ == '__main__':
    app.run(debug=True)