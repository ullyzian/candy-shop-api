from datetime import datetime
from api import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    order_item = db.relationship("OrderItem", backref="user", lazy="dynamic")
    order = db.relationship("Order", backref="user", lazy="dynamic")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    order_item = db.relationship("OrderItem", uselist=False, backref="item")

    def __repr__(self):
        return f"<Item {self.title}>"


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    order = db.relationship("Order", backref="orderitem")
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f"<OrderItem {self.item.title}>"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Item {self.user.username}>"
