from flask_restplus import Namespace, Resource, fields
from flask import request
from .strings.capitalize import capitalize

api = Namespace('strings', description='String related operations')

string = api.model('String', {
  'function': fields.String(description='The name of the operation'),
  'output': fields.String(description='The output of the operation')
})

class Output(object):
  def __init__(self, output, function):
    self.output = output
    self.function = function

@api.route('/capitalize', methods=['POST'])
@api.param('input', 'The string input', _in='body')
@api.response(404, 'Resource not found')
class Capitalize(Resource):
  @api.doc('capitalize_string')
  @api.marshal_with(string)
  def post(self):
    """
    Capitalizes the first letter of a string.

    Capitalizes the fist letter of the sring and then adds it with rest of the string. Omit the lower_rest parameter to keep the rest of the string intact, or set it to true to convert to lowercase.
    """
    req_data = request.get_json()
    input = req_data['input']
    output = capitalize(input)
    return Output(output=output, function='Capitalize')
