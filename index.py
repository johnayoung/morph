# app.py
from flask import Flask
from flask_restplus import Resource, Api, fields
from flask.json import jsonify
from flask import request
from werkzeug.contrib.fixers import ProxyFix
from apis import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)