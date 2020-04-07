from flask import jsonify
from api.models import Order
from api.shemas import order_schema, orders_schema
from api import app, db


@app.route("/orders", methods=["POST"])
def add_order():
    new_order = Order()

    db.session.add(new_order)
    db.session.commit()

    return order_schema.dump(new_order)


@app.route("/orders/<id>", methods=["GET"])
def get_order(id):
    order = Order.query.get(id)
    return order_schema.dump(order)


@app.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    result = orders_schema.dump(orders)
    return jsonify(result)


@app.route("/orders/<id>", methods=["DELETE"])
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()

    return order_schema.dump(order)

