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

print(capitalize('testing yeahhh'))

class Output(object):
  def __init__(self, output, function):
    self.output = output
    self.function = function

@app.route('/strings/capitalize', methods=['POST'])
def cap():
    req_data = request.get_json()
    input = req_data['input']
    output = {
        'function': 'Capitalize', 
        'output': capitalize(input)
    }
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)