from flask_restplus import Namespace, Resource, fields
from flask import request
import asyncio
import requests

api = Namespace('Utilities', description='Utility related operations')

utilities = api.model('Utility', {
  'function': fields.String(description='The name of the operation'),
  'output': fields.String(description='The output of the operation')
})

class Output(object):
  def __init__(self, output, function):
    self.output = output
    self.function = function

@api.route('/weather', methods=['GET'])
@api.param('query', 'text to search for', _in='query')
@api.response(404, 'Resource not found')
class Weather(Resource):
  @api.doc('utility_weather')
  @api.marshal_with(utilities)
  def get(self):
    query = request.args.get('query')
    res = requests.get('https://www.metaweather.com/api/location/search/?query=' + query)
    output = res.json()
    print('res is printing!')

    return Output(output=output, function='Bubble Sort')