from flask import jsonify, request
from functools import wraps
import jwt
from api import app
from api.models import User


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        bearerHeader = None
        try:
            [bearerHeader, token] = request.headers["Authorization"].split(" ")
        except:
            return jsonify({"message": "token is missing"})

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = User.query.filter_by(id=data["user_id"]).first()
        except:
            return jsonify({"message": "token is invalid"})

        return f(current_user, *args, **kwargs)

    return decorator
