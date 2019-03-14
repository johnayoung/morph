# app.py
from flask import Flask
from flask_restplus import Resource, Api, fields
from flask.json import jsonify
from flask import request
import requests
import json
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
from capitalize import capitalize
from capitalize_every_word import title_extended as capitalize_every_word
from uppercase import uppercase
from lowercase import lowercase
from byte_size import byte_size
from pipe import pipeFunctions

function_list = {
    'capitalize': capitalize,
    'capitalize_every_word': capitalize_every_word,
    'uppercase': uppercase,
    'lowercase': lowercase,
    'byte_size': byte_size
}

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
    title='Morph',
    version='1.0',
    description='A standardized RESTful Utility API',
    base_url='https://morph.now.sh/'
)

WIT_CLIENT_TOKEN = 'VPQ6T6AJS7BUPCOG5GXUNYDHN6DVJGF7'

# Define standardized rest output
class Output(object):
  def __init__(self, output, function):
    self.output = output
    self.function = function

# Define API namespaces: Strings, Lists, Math, etc...
strings = api.namespace('strings', description='String related operations')

# Define namespace output models
stringModel = api.model('Strings', {
    'function': fields.String,
    'output': fields.String,
})

@api.route('/morph')
@api.param('input', 'The string input', _in='query')
class Morph(Resource):
    @api.marshal_with(stringModel)
    def get(self):
        req_input = request.args.get('input')
        endpoint = 'https://api.wit.ai/message?v=20170307&q={}'.format(req_input)
        headers = {"Authorization": "Bearer VPQ6T6AJS7BUPCOG5GXUNYDHN6DVJGF7"}
        wit = requests.get(endpoint, headers=headers).json()
        entities = wit['entities']
        api_methods = entities['api_method']
        funcList = []
        for methods in api_methods:
            funcList.append(methods['value'])
        input = entities['input'][0]['value']

        funcDict = {}
        for fns in funcList:
            funcDict[fns] = function_list.get(fns)
        print(funcDict)
        output = pipeFunctions(input, *funcDict.values())
        # output = capitalize('anything')
        # print(output)
        return Output(output=output, function='The almighty Morph')

# Start string routes
@strings.route('/capitalize')
@api.param('input', 'The string input', _in='query')
class strCap(Resource):
    @api.marshal_with(stringModel)
    def get(self, **kwargs):
        input = request.args.get('input')
        output = capitalize(input)
        return Output(output=output, function='Capitalize')

@strings.route('/capitalize_every_word')
@api.param('input', 'The string input', _in='query')
class strCapAll(Resource):
    @api.marshal_with(stringModel)
    def get(self, **kwargs):
        input = request.args.get('input')
        output = capitalize_every_word(input)
        return Output(output=output, function='Capitalize Every Word')

@strings.route('/uppercase')
@api.param('input', 'The string input', _in='query')
class strUppercase(Resource):
    @api.marshal_with(stringModel)
    def get(self, **kwargs):
        input = request.args.get('input')
        output = uppercase(input)
        return Output(output=output, function='Uppercase')

@strings.route('/lowercase')
@api.param('input', 'The string input', _in='query')
class strLowercase(Resource):
    @api.marshal_with(stringModel)
    def get(self, **kwargs):
        input = request.args.get('input')
        output = lowercase(input)
        return Output(output=output, function='Lowercase')

@strings.route('/byte_size')
@api.param('input', 'The string input', _in='query')
class strByte(Resource):
    @api.marshal_with(stringModel)
    def get(self, **kwargs):
        input = request.args.get('input')
        output = byte_size(input)
        return Output(output=output, function='Byte Size')

if __name__ == '__main__':
    app.run(debug=True)