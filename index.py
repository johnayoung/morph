# app.py
from flask import Flask
from flask_restplus import Resource, Api, fields
from flask.json import jsonify
from flask import request
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
from capitalize import capitalize

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
    title='Morph',
    version='1.0',
    description='A standardized RESTful Utility API',
)

@api.route('/hello_world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/capitalize')
class Cap(Resource):
    model = api.model('Capitalize', {
        'function': fields.String,
        'output': fields.String,
    })
    @api.marshal_with(model, envelope='resource')
    def get(self, **kwargs):
        output = capitalize('diabolical')
        return output

if __name__ == '__main__':
    app.run(debug=True)