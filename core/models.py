from datetime import datetime
from dataclasses import dataclass
from core import db as models


@dataclass
class User(models.Model):
    id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime

    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(60), index=True, unique=True)
    email = models.Column(models.String(120), index=True, unique=True)
    password_hash = models.Column(models.String(128))
    created_at = models.Column(models.DateTime, index=True, default=datetime.utcnow)
    order_item = models.relationship("OrderItem", backref="user", lazy="dynamic")
    order = models.relationship("Order", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"


@dataclass
class Item(models.Model):
    id: int
    title: str
    price: float
    description: str

    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String(50))
    price = models.Column(models.Float)
    description = models.Column(models.Text)
    order_item = models.relationship("OrderItem", uselist=False, backref="item")

    def __repr__(self):
        return f"<Item {self.title}>"


class OrderItem(models.Model):

    id = models.Column(models.Integer, primary_key=True)
    item_id = models.Column(models.Integer, models.ForeignKey("item.id"))
    user_id = models.Column(models.Integer, models.ForeignKey("user.id"))
    order_id = models.Column(models.Integer, models.ForeignKey("order.id"))
    order = models.relationship("Order", backref="orderitem")
    quantity = models.Column(models.Integer)

    def __repr__(self):
        return f"<OrderItem {self.item.title}>"


@dataclass
class Order(models.Model):
    id: int
    user_id: int
    created_at: datetime

    id = models.Column(models.Integer, primary_key=True)
    user_id = models.Column(models.Integer, models.ForeignKey("user.id"))
    created_at = models.Column(models.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Item {self.user.username}>"
