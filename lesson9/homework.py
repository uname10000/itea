import mongoengine as me
from flask import Flask
from flask_restful import Api

from resurses import StudentsResources

me.connect('lesson_9')
app = Flask(__name__)
api = Api(app)

api.add_resource(StudentsResources, '/student', '/student/<string:student_id>')

app.run(debug=True)