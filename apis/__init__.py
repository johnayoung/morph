from flask_restplus import Api

from .stringApi import api as strings
from .listApi import api as lists

api = Api(
  title='Morph',
  version='1.0',
  description='A standardized RESTful Utility API',
)

api.add_namespace(strings, path='/strings')
api.add_namespace(lists, path='/lists')