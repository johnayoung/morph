from flask_restplus import Api

from .stringApi import api as strings

api = Api(
  title='Morph',
  version='1.0',
  description='A standardized RESTful Utility API'
)

api.add_namespace(strings, path='/api/strings')