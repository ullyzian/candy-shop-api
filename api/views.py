from flask import request, jsonify
from api.models import User
from api.shemas import user_shema, users_shema
from api import app, db


@app.route("/users", methods=["POST"])
def add_user():
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    new_user = User(username, email, password)

    username_exists = db.session.query(
        db.session.query(User).filter_by(username=new_user.username).exists()
    ).scalar()

    email_exists = db.session.query(
        db.session.query(User).filter_by(email=new_user.email).exists()
    ).scalar()

    if username_exists:
        return {"error": "This username already registered"}
    elif email_exists:
        return {"error": "This email already registered"}
    else:
        db.session.add(new_user)
        db.session.commit()

        return user_shema.dump(new_user)


@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return user_shema.dump(user)


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    result = users_shema.dump(users)
    return jsonify(result)


@app.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_shema.dump(user)


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)

    username = request.json["username"]
    email = request.json["email"]

    username_exists = db.session.query(
        db.session.query(User).filter_by(username=username).exists()
    ).scalar()

    email_exists = db.session.query(
        db.session.query(User).filter_by(email=email).exists()
    ).scalar()
    if user.username == username:
        return {"error": "Enter new username"}
    elif user.email == email:
        return {"error": "Enter new email"}
    elif username_exists:
        return {"error": "This username already registered"}
    elif email_exists:
        return {"error": "This email already registered"}
    else:
        user.username = username
        user.email = email
        user.password = request.json["password"]

        db.session.commit()

        return user_shema.dump(user)
