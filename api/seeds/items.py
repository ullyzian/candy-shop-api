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
            "title": "Skittles Fruits",
            "price": 4.99,
            "description": "Skittles consist of hard sugar shells imprinted with the letter 'S'. The interior consists mainly of sugar, corn syrup, and hydrogenated palm kernel oil along with fruit juice, citric acid, natural and artificial flavors.",
            "image_path": "https://imgur.com/m6jeGJ5.jpg",
        },
        {
            "title": "Skittles Crazy Sours",
            "price": 4.99,
            "description": "Skittles consist of hard sugar shells imprinted with the letter 'S'. They're a bit different in that they don't look different, but have a different set of flavors from the Fruits set but no tangy coating.",
            "image_path": "https://i.imgur.com/RFKY2gT.png",
        },
        {
            "title": "Skittles Wild Berry",
            "price": 4.99,
            "description": "Skittles consist of hard sugar shells imprinted with the letter 'S'. Bite-size, colorful chewy candies. Taste the Rainbow—Wild Berry Skittles includes berry punch, strawberry, melon berry, wild cherry, and raspberry flavors.",
            "image_path": "https://i.imgur.com/f59lUj2.jpg",
        },
        {
            "title": "Skittles Brightside",
            "price": 4.99,
            "description": "Skittles consist of hard sugar shells imprinted with the letter 'S'.  Candy includes kiwi banana, watermelon, paradise punch, pink lemonade, and tangerine flavors",
            "image_path": "https://i.imgur.com/RWfUoQW.jpg",
        },
        {
            "title": "M&M's Minis",
            "price": 3.99,
            "description": "M&M's are multi-colored button-shaped chocolates, each of which has the letter 'm' printed in lower case in white on one side, consisting of a candy shell surrounding a filling which varies depending upon the variety of M&M's.",
            "image_path": "https://i.imgur.com/4ITjs8j.jpg",
        },
        {
            "title": "Twix Box",
            "price": 12.99,
            "description": "Twix is a chocolate bar made by Mars, Inc., consisting of a biscuit applied with other confectionery toppings and coatings (most frequently caramel and milk chocolate). Twix are packaged with two or four bars in a wrapper. Miniature and other variations of Twix bars are also available.",
            "image_path": "https://i.imgur.com/0HsdSmD.jpg",
        },
        {
            "title": "Prince Polo XXL Classic Box ",
            "price": 7.99,
            "description": "Prince Polo is a Polish chocolate bar It is a chocolate-covered wafer, with four layers of wafer joined by three layers of chocolate-flavored filling; Packed in a metallic gold-colored wrapper.",
            "image_path": "https://i.imgur.com/qQKfu8u.jpg",
        },
        {
            "title": "Prince Polo XXL Milk Box",
            "price": 7.99,
            "description": "Prince Polo is a Polish chocolate bar It is a chocolate-covered wafer, with four layers of wafer joined by three layers of chocolate-flavored filling; Packed in a metallic gold-colored wrapper.",
            "image_path": "https://i.imgur.com/Rk8kDbs.jpg",
        },
        {
            "title": "Prince Polo XXL Nuts Box",
            "price": 7.99,
            "description": "Prince Polo is a Polish chocolate bar It is a chocolate-covered wafer, with four layers of wafer joined by three layers of chocolate-flavored filling; Packed in a metallic gold-colored wrapper.",
            "image_path": "https://i.imgur.com/nvYVnXw.jpg",
        },
        {
            "title": "Milka Alpine Milk ",
            "price": 29.99,
            "description": "Milka Alpine Milk Chocolate is has the best quality of Alpine Milk added to give it that rich, creamy flavor. Alpine Milk is the delicious, smooth chocolate delight from 100% Alpine Milk, the classic for all chocolate fans.",
            "image_path": "https://i.imgur.com/J6mNhSD.jpg",
        },
        {
            "title": "Milka OREO bars",
            "price": 21.99,
            "description": "Delicious Milka Alpine Milk Chocolate with Oreo",
            "image_path": "https://i.imgur.com/3MYhogx.jpg",
        },
        {
            "title": "Present FISH Box",
            "price": 37.99,
            "description": "Box includes different chewing worms",
            "image_path": "https://i.imgur.com/RZBNQvR.jpg",
        },
        {
            "title": "Birthday Box ",
            "price": 50.99,
            "description": "Box for sweet tooth, why celebrate their birthday",
            "image_path": "https://i.imgur.com/bOPECW9.jpg",
        },

    ]

    # Adding items to Item table
    for item in items:
        instance = Item(
            item["title"], item["price"], item["description"], item["image_path"]
        )
        db.session.add(instance)

    db.session.commit()
