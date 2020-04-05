from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from api.models import db, User

view = Blueprint("views", __name__)
api = Api(view)

parser = reqparse.RequestParser()
parser.add_argument("username")
parser.add_argument("email")


class UserView(Resource):
    def get(self):
        return User.get_delete_put_post()

    def post(self):
        args = parser.parse_args()
        user = User(username=args["username"], email=args["email"])
        exists = db.session.query(
            db.exists().where(
                User.username == user.username or User.email == user.email
            )
        ).scalar()
        if exists:
            return "User already registered", 201
        db.session.add(user)
        db.session.commit()
        return "User added", 200


api.add_resource(UserView, "/")

