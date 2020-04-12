from sqlalchemy import event
from api import db
from api.models import Item


@event.listens_for(Item.__table__, 'after_create')
def insert_items(target, connection, **kwargs):
    # Creating list of dictionaries (items)
    items = [
        {
            "title": "Snickers box",
            "price": 12.99,
            "description": "This is the box of very sweet candies called snickers",
            "image_path": "https://pakerszop.pl/public/assets//snickers-hi-protein-bar.jpg"
        },
        {
            "title": "Bounty box",
            "price": 15.99,
            "description": "This is the box of very sweet candies called bounty",
            "image_path": "https://images-na.ssl-images-amazon.com/images/I/51H3bd4ChOL.jpg"
        },
        {
            "title": "Mars box",
            "price": 10.99,
            "description": "This is the box of very sweet candies called mars",
            "image_path": "https://www.tajonline.com/images/product_images/sgf79_large3.jpg"
        },
        {
            "title": "M&M's Chocolate Candies",
            "price": 3.99,
            "description": "Chocolate candies with a tasty nut inside",
            "image_path": "https://target.scene7.com/is/image/Target/GUEST_4714fef1-960f-48db-a609-6a09aa04db7a?fmt=pjpeg&wid=1400&qlt=80"
        },
        {
            "title": "Skittles fruits",
            "price": 4.99,
            "description": "Chocolate candies with a tasty nut inside",
            "image_path": "https://images.shopdutyfree.com/image/upload//v1531470964/030/001/002/4009900479134/4009900479134_1_default_default.jpg"
        }
    ]

    # Adding items to Item table
    for item in items:
        db.session.add(Item(item["title"], item["price"], item["description"], item["image_path"]))

    db.session.commit()


