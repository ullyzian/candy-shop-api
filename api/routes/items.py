from flask import request, jsonify
from api.models import Item, tags_table, Tag, TagItemRel
from api.shemas import item_schema, items_schema, tag_item_rel, tags_items_rel
from api import app, db
from sqlalchemy.sql import func


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

    # Basic query
    query = db.session.query(Item, func.count(Item.id)).group_by(Item.id)

    if search_text is not None:
        search_pattern = "%{}%".format(search_text)
        # Updating query to select items that satisfy pattern
        query = query\
        .filter(Item.name.like(search_pattern))

    if filter_arg is not None:
        filter_tags = filter_arg.split(";")
        # Updating query to join tables and filter tags
        query = query \
            .join(TagItemRel, Item.id == TagItemRel.item_id) \
            .join(Tag, TagItemRel.tag_id == Tag.id) \
            .filter(Tag.label.in_(filter_tags))

    # Executing query
    query_response = query.all()
    # Query returns tuples list, tuple format: (item, # of matched filter)

    result = set()
    for [item, matched_filters] in query_response:
        # In case filters were passed
        if filter_arg is not None:
            # If # of matched tags is smaller then # of passed filters - do not include them into result
            if len(filter_arg.split(";")) <= matched_filters:
                result.add(item)
        else:
            result.add(item)

    result = items_schema.dump(result)

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
