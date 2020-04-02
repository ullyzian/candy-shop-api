import time
from flask import Blueprint
from flask_restful import Api, Resource
from api.models import User

view = Blueprint("views", __name__)
api = Api(view)

class Time(Resource):
    def get(self):
        return {
            'time': time.time(),
            'user': User.query.all()
            }

api.add_resource(Time, '/time')