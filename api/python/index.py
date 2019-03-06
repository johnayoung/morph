# app.py
from flask import Flask
from flask_restplus import Resource, Api, fields
from flask.json import jsonify
from werkzeug.contrib.fixers import ProxyFix
from database import db_session
from models import BlogPost
from max_n import max_n
from bubble_sort import bubble_sort

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
          version='0.1',
          title='Our sample API',
          description='This is our sample API'
)

@api.route('/hello_world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/blog_posts')
class BlogPosts(Resource):
    model = api.model('BlogPost', {
        'id': fields.Integer,
        'title': fields.String,
        'post': fields.String,
    })
    @api.marshal_with(model, envelope='resource')
    def get(self, **kwargs):
        return BlogPost.query.all()

@app.route("/max")
def status():
  return jsonify(max_n([1, 2, 3]))

@app.route('/bubble_sort')
def bubble():
    lst = [54,26,93,17,77,31,44,55,20]
    bubble_sort(lst)
    return jsonify(lst)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)