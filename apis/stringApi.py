from flask_restplus import Namespace, Resource, fields
from flask import request
from .strings.capitalize import capitalize
from .strings.lowercase import lowercase
from .strings.uppercase import uppercase
from .strings.pipe import pipeFunctions
from .strings.words import words

# Required for the pipe functionality to prevent security concerns
function_mappings = {
  'capitalize': capitalize,
  'lowercase': lowercase,
  'uppercase': uppercase,
  'words': words
}

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

@api.route('/pipe', methods=['GET'])
@api.param('input', 'The string input', _in='query')
@api.param('funcs', 'The left-to-right functions to perform on the input', _in='query')
@api.response(404, 'Resource not found')
class Pipe(Resource):
  @api.doc('string_pipe')
  @api.marshal_with(string)
  def get(self):
    """
    Performs left-to-right function composition on a string.

    Examples:
    ----------
    Request:
    ```
    morph.now.sh/strings/pipe?funcs=capitalize,uppercase&input=johnny
    ```

    Response:
    ```
    ['Johnny', 'JOHNNY']
    ```

    """
    input = request.args.get('input')
    funcs = request.args.get('funcs')
    funcList = funcs.split(',')
    funcDict = {}
    for fns in funcList:
      funcDict[fns] = function_mappings.get(fns)
    # funcDict = map(lambda: function_mappings.get(x), funcList)
    print(funcDict)
    output = pipeFunctions(input, *funcDict.values())
    return Output(output=output, function='Pipe')