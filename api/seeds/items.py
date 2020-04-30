from sqlalchemy import event
from api import db
from api.models import Item, tags_table, Tag


@event.listens_for(tags_table, "after_create")
def insert_items(target, connection, **kwargs):
    # Creating list of dictionaries (items)
    items = [
        {
            "title": "Snickers box",
            "price": 12.99,
            "description": "This is the box of very sweet candies called snickers",
            "image_path": "https://imgur.com/Cf2LfAr.jpg",
            "tags": [{"id": 1, "label": "Chocolate"}, {"id": 2, "label": "Caramel"}],
        },
        {
            "title": "Bounty box",
            "price": 15.99,
            "description": "This is the box of very sweet candies called bounty",
            "image_path": "https://imgur.com/TfGb3t4.jpg",
            "tags": [{"id": 1, "label": "Chocolate"}],
        },
        {
            "title": "M&M's Chocolate Candies",
            "price": 3.99,
            "description": "Chocolate candies with a tasty nut inside",
            "image_path": "https://imgur.com/8sMeZLn.jpg",
            "tags": [{"id": 1, "label": "Chocolate"}],
        },
        {
            "title": "Skittles fruits",
            "price": 4.99,
            "description": "Tasty candie, kinda sour",
            "image_path": "https://imgur.com/m6jeGJ5.jpg",
            "tags": [],
        },
    ]

    # Adding items to Item table
    for item in items:
        query = []
        for tag in item["tags"]:
            query.append(Tag.query.filter_by(label=tag["label"]).one())
        instance = Item(
            item["title"], item["price"], item["description"], item["image_path"], query
        )
        db.session.add(instance)

    db.session.commit()
