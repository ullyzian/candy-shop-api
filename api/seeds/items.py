from sqlalchemy import event
from api import db
from api.models import Item, Tag


@event.listens_for(Item.__table__, "after_create")
def insert_items(target, connection, **kwargs):
    # Creating list of dictionaries (items)
    items = [
        {
            "title": "Snickers box",
            "price": 12.99,
            "description": "Snickers is a brand name chocolate bar made by the American company Mars, Incorporated, consisting of nougat topped with caramel and peanuts that has been enrobed in milk chocolate.",
            "image_path": "https://imgur.com/Cf2LfAr.jpg",
        },
        {
            "title": "Bounty box",
            "price": 15.99,
            "description": "Bounty is a chocolate bar manufactured by Mars, Incorporated. It was introduced in 1951 in the United Kingdom and Canada. Bounty has a coconut filling enrobed with milk chocolate.",
            "image_path": "https://imgur.com/TfGb3t4.jpg",
        },
        {
            "title": "M&M's Chocolate Candies",
            "price": 3.99,
            "description": "M&M's are multi-colored button-shaped chocolates, each of which has the letter 'm' printed in lower case in white on one side, consisting of a candy shell surrounding a filling which varies depending upon the variety of M&M's.",
            "image_path": "https://imgur.com/8sMeZLn.jpg",
        },
        {
            "title": "Skittles fruits",
            "price": 4.99,
            "description": "Skittles consist of hard sugar shells imprinted with the letter 'S'. The interior consists mainly of sugar, corn syrup, and hydrogenated palm kernel oil along with fruit juice, citric acid, natural and artificial flavors.",
            "image_path": "https://imgur.com/m6jeGJ5.jpg",
        },
    ]

    # Adding items to Item table
    for item in items:
        instance = Item(
            item["title"], item["price"], item["description"], item["image_path"]
        )
        db.session.add(instance)

    db.session.commit()
