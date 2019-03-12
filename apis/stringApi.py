from flask_restplus import Namespace, Resource, fields
from flask import request
from .strings.capitalize import capitalize
from .strings.lowercase import lowercase
from .strings.uppercase import uppercase

api = Namespace('Strings', description='String related operations')

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
  @api.doc('string_capitalize')
  @api.marshal_with(string)
  def post(self):
    """
    Capitalizes the first letter of a string.

    Capitalizes the first letter of the string and then adds it with rest of the string. Omit the lower_rest parameter to keep the rest of the string intact, or set it to true to convert to lowercase.

    Function:
    ----------
    ```
    def capitalize(string, lower_rest=False):
      return string[:1].upper() + (string[1:].lower() if lower_rest else string[1:])
    ```

    Examples:
    ----------
    ```
    morph.now.sh/strings/capitalize

    body: {
      "input": "tester"
    }
    ```

    """
    req_data = request.get_json()
    input = req_data['input']
    output = capitalize(input)
    return Output(output=output, function='Capitalize')

@api.route('/uppercase', methods=['POST'])
@api.param('input', 'The string input', _in='body')
@api.response(404, 'Resource not found')
class Uppercase(Resource):
  @api.doc('string_uppercase')
  @api.marshal_with(string)
  def post(self):
    """
    Uppercase all letters of a string.

    Convert the given string to upper case
    """
    req_data = request.get_json()
    input = req_data['input']
    output = uppercase(input)
    return Output(output=output, function='Uppercase')
