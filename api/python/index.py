from flask import Flask
from flask.json import jsonify
app = Flask(__name__)

# test

def max_n(lst, n=1, reverse=True):
  return sorted(lst, reverse=reverse)[:n]

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/max")
def status():
  return jsonify(max_n([1, 2, 3]))