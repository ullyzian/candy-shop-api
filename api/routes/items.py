from flask import request, jsonify
from api.models import Item, Tag, TagItemRel
from api.shemas import items_schema
from api import app, db
from sqlalchemy.sql import func


@app.route("/items/<ids>", methods=["GET"])
def get_items_by_id(ids):
    include = request.args.get("include")
    id_arr = ids.split(",")
    items = Item.query.filter(Item.id.in_(id_arr)).all()

    items = items_schema.dump(items)

    if include is not None:
        properties_to_include = include.split(";")
        if "tags" in properties_to_include:
            db_tags = (
                db.session.query(TagItemRel.item_id, Tag.label)
                .join(TagItemRel, Tag.id == TagItemRel.tag_id)
                .filter(TagItemRel.item_id.in_(id_arr))
                .all()
            )

            hash_tags = {}
            # Formatting result to a hash table
            for [item_id, tag_name] in db_tags:
                if item_id in hash_tags:
                    hash_tags[item_id].append(tag_name)
                else:
                    hash_tags[item_id] = [tag_name]

            # Appending tags to items
            for item in items:
                item["tags"] = hash_tags[item["id"]]

    return jsonify({"result": items})


@app.route("/items", methods=["GET"])
def get_items():
    search_text = request.args.get("search")
    filter_arg = request.args.get("filter")

    # Basic query
    query = db.session.query(Item, func.count(Item.id)).group_by(Item.id)

    if search_text is not None:
        search_pattern = "%{}%".format(search_text)
        # Updating query to select items that satisfy pattern
        query = query.filter(Item.name.like(search_pattern))

    if filter_arg is not None:
        filter_tags = filter_arg.split(";")
        # Updating query to join tables and filter tags
        query = (
            query.join(TagItemRel, Item.id == TagItemRel.item_id)
            .join(Tag, TagItemRel.tag_id == Tag.id)
            .filter(Tag.label.in_(filter_tags))
        )

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
