from flask import request, jsonify
from api.models import OrderItem
from api.shemas import orderitem_schema, orderitems_schema
from api import app, db


@app.route("/orderitems", methods=["POST"])
def add_orderitem():
    item_id = request.json["item_id"]
    order_id = request.json["order_id"]
    quantity = request.json["quantity"]

    new_orderitem = OrderItem(item_id, order_id, quantity)

    db.session.add(new_orderitem)
    db.session.commit()

    return orderitem_schema.dump(new_orderitem)


@app.route("/orderitems/<id>", methods=["GET"])
def get_orderitem(id):
    item = OrderItem.query.get(id)
    return orderitem_schema.dump(item)


@app.route("/orderitems", methods=["GET"])
def get_orderitems():
    items = OrderItem.query.all()
    result = orderitems_schema.dump(items)
    return jsonify(result)


@app.route("/orderitems/<id>", methods=["DELETE"])
def delete_orderitem(id):
    item = OrderItem.query.get(id)
    db.session.delete(item)
    db.session.commit()

    return orderitem_schema.dump(item)


@app.route("/orderitems/<id>", methods=["PUT"])
def update_orderitem(id):
    item = OrderItem.query.get(id)

    item.item_id = request.json["item_id"]
    item.order_id = request.json["order_id"]
    item.quantity = request.json["quantity"]

    db.session.commit()

    return orderitem_schema.dump(item)
