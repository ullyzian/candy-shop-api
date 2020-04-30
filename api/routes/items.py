from flask import request, jsonify
from api.models import Item, tags_table, Tag
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
    filter_arg = request.args.get("filter")
    if search_text is not None:
        search_pattern = "%{}%".format(search_text)
        items = Item.query.filter(Item.name.like(search_pattern)).all()
    elif filter_arg is not None:
        filter_tags = filter_arg.split(";")
        tags = Tag.query.filter(Tag.label.in_(filter_tags)).all()
        items_array = [Item.query.filter(Item.tags.any(id=tag.id)).all() for tag in tags]
        items = set([item for i in items_array for item in i])
    else:
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

    item.name = request.json["name"]
    item.price = request.json["price"]
    item.description = request.json["description"]

    db.session.commit()

    return item_schema.dump(item)
