from api import app, db
import jwt
import datetime
from api.models import User, Order, OrderItem, Item
from api.shemas import user_schema, orderitems_schema, item_schema
from flask import request, jsonify
from api.decorators import token_required
from flask_cors import cross_origin


@app.route("/login", methods=["POST"])
@cross_origin()
def login():
    username = request.json["username"]
    password = request.json["password"]

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

@app.route("/register", methods=["POST"])
@cross_origin()
def register():
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]

    user = User.query.filter(User.username == username).first()
    # checking if entered username exists
    if not user:
        try:
            new_user = User(username, email)
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()
        except:
            return jsonify({"message": "An error occured, try again"})

        # token generation
        token = jwt.encode(
            {
                "user_id": new_user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=200),
            },
            app.config["SECRET_KEY"],
        )
        return jsonify({"token": token.decode("UTF-8")})

    else:
        return {"message": "User already exists"}


@app.route("/user", methods=["GET"])
@cross_origin()
@token_required
def get_user(current_user):
    user = user_schema.dump(current_user)
    user = {"id": user["id"], "email": user["email"]}
    return user


@app.route("/profile", methods=["GET"])
@cross_origin()
@token_required
def profile(current_user):
    profile = user_schema.dump(current_user)
    for order in profile["orders"]:
        order_items = OrderItem.query.filter_by(order_id=order["id"]).all()
        items = []
        for order_item in order_items:
            query = Item.query.filter_by(id=order_item.item_id).one()
            schema = item_schema.dump(query)
            schema["quantity"] = order_item.quantity
            items.append(schema)
        order["items"] = items
    del profile["password"]
    return profile
