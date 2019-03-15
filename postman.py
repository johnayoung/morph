from flask import Flask, json, url_for
from flask_restplus import Resource, Api

from index import app, api

with app.test_request_context():
  urlvars = False  # Build query strings in URLs
  swagger = True  # Export Swagger specifications
  data = api.as_postman(urlvars=urlvars, swagger=swagger)
  f = open('postman_import.json', 'w')
  f.write(json.dumps(data))
