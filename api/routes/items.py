from flask import request, jsonify
from api.models import Item
from api.shemas import item_schema, items_schema
from api import app, db


@app.route("/items", methods=["POST"])
def add_item():
    title = request.json["title"]
    price = request.json["price"]
    description = request.json["description"]

    new_item = Item(title, price, description)

    db.session.add(new_item)
    db.session.commit()

    return item_schema.dump(new_item)


@app.route("/items/<id>", methods=["GET"])
def get_item(id):
    item = Item.query.get(id)
    return item_schema.dump(item)


@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    result = items_schema.dump(items)
    return jsonify({"result": result})


@app.route("/items/<id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()

    return item_schema.dump(item)


@app.route("/items/<id>", methods=["PUT"])
def update_item(id):
    item = Item.query.get(id)

    item.title = request.json["title"]
    item.price = request.json["price"]
    item.description = request.json["description"]

    db.session.commit()

    return item_schema.dump(item)
