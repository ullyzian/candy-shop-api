from api import app, db
import jwt
import datetime
from api.models import User
from api.shemas import user_schema
from flask import request, jsonify
from api.decorators import token_required
from flask_cors import cross_origin



@app.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    auth = request.authorization

    user = User.query.filter(User.username == username).first()
    # checking if entered username exists
    if user:
        # checking password
        if user.check_password(password):
            # token generation
            token = jwt.encode(
                {
                    "user_id": user.id,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=200),
                },
                app.config["SECRET_KEY"],
            )
            return jsonify({"token": token.decode("UTF-8")})
        else:
            return {"message": "Incorrect password"}
    else:
        return {"message": "User does not exists"}


@app.route("/user", methods=["GET"])
@cross_origin()
@token_required
def get_user(current_user):
    user = user_schema.dump(current_user)
    user = {
        'id': user['id'],
        'email': user['email']
    }
    return user


@app.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    user = user_schema.dump(current_user)

    return user
