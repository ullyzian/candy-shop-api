from flask import request, jsonify
from api.models import Item
from api.shemas import item_schema, items_schema
from api import app, db


@app.route("/items", methods=["POST"])
def add_item():
    name = request.json["name"]
    price = request.json["price"]
    description = request.json["description"]

    new_item = Item(name, price, description)

    db.session.add(new_item)
    db.session.commit()

    return item_schema.dump(new_item)


@app.route("/items/<ids>", methods=["GET"])
def get_items_by_id(ids):
    id_arr = ids.split(",")
    items = Item.query.filter(Item.id.in_(id_arr)).all()
    result = items_schema.dump(items)
    return jsonify({"result": result})


@app.route("/items", methods=["GET"])
def get_items():
    search_text = request.args.get("search")
    search_pattern = "%{}%".format(search_text) if search_text else "%"
    items = Item.query.filter(Item.name.like(search_pattern)).all()
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

    item.name = request.json["name"]
    item.price = request.json["price"]
    item.description = request.json["description"]

    db.session.commit()

    return item_schema.dump(item)
