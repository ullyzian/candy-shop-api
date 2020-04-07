from datetime import datetime
from api import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    order_item = db.relationship("OrderItem", uselist=False, backref="item")

    def __init__(self, title, price, description):
        self.title = title
        self.price = price
        self.description = description

    def __repr__(self):
        return f"<Item {self.title}>"


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    order = db.relationship("Order", backref="orderitem")
    quantity = db.Column(db.Integer)

    def __init__(self, *args):
        self.item_id = args[0]
        self.order_id = args[1]
        self.quantity = args[2]

    def __repr__(self):
        return f"<OrderItem {self.item.title}>"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Item {self.user.username}>"
