from flask import jsonify, request
from api.models import Order, OrderItem
from api.shemas import order_schema, orders_schema
from api import app, db


@app.route("/order", methods=["POST"])
def add_order():
    email = request.json["mail"]
    order_items = request.json["items"]

    new_order = Order(email)

    db.session.add(new_order)
    db.session.commit()

    for item in order_items:
        instance = OrderItem(item["id"], new_order.id, item["quantity"])
        db.session.add(instance)

    db.session.commit()

    return order_schema.dump(new_order)


@app.route("/order/<id>", methods=["GET"])
def get_order(id):
    order = Order.query.get(id)
    return order_schema.dump(order)


@app.route("/order", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    result = orders_schema.dump(orders)
    return jsonify(result)


@app.route("/order/<id>", methods=["DELETE"])
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()

    return order_schema.dump(order)

