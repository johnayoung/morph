# app.py
from flask import Flask
from flask_restplus import Resource, Api, fields
from flask.json import jsonify
from flask import request
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
from capitalize import capitalize
from uppercase import uppercase

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
    title='Morph',
    version='1.0',
    description='A standardized RESTful Utility API',
)

class Output(object):
  def __init__(self, output, function):
    self.output = output
    self.function = function

strings = api.namespace('strings', description='String related operations')

@api.route('/hello_world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@strings.route('/capitalize')
@api.param('input', 'The string input', _in='query')
class Cap(Resource):
    model = api.model('Capitalize', {
        'function': fields.String,
        'output': fields.String,
    })
    @api.marshal_with(model)
    def get(self, **kwargs):
        input = request.args.get('input')
        output = capitalize(input)
        return Output(output=output, function='Capitalize')

@strings.route('/uppercase')
@api.param('input', 'The string input', _in='query')
class strUppercase(Resource):
    model = api.model('Uppercase', {
        'function': fields.String,
        'output': fields.String,
    })
    @api.marshal_with(model)
    def get(self, **kwargs):
        input = request.args.get('input')
        output = uppercase(input)
        return Output(output=output, function='Uppercase')

if __name__ == '__main__':
    app.run(debug=True)