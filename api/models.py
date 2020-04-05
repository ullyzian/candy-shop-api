from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_serialize import FlaskSerializeMixin

models = db = SQLAlchemy()

FlaskSerializeMixin.db = db

class User(FlaskSerializeMixin, models.Model):
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(60), index=True, unique=True)
    email = models.Column(models.String(120), index=True, unique=True)
    password_hash = models.Column(models.String(128))
    created_at = models.Column(models.DateTime, index=True, default=datetime.utcnow)
    order_item = models.relationship("OrderItem", backref="user", lazy="dynamic")
    order = models.relationship("Order", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"


class Item(FlaskSerializeMixin, models.Model):
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String(50))
    price = models.Column(models.Float)
    description = models.Column(models.Text)
    order_item = models.relationship("OrderItem", uselist=False, backref="item")

    def __repr__(self):
        return f"<Item {self.title}>"


class OrderItem(FlaskSerializeMixin, models.Model):
    id = models.Column(models.Integer, primary_key=True)
    item_id = models.Column(models.Integer, models.ForeignKey("item.id"))
    user_id = models.Column(models.Integer, models.ForeignKey("user.id"))
    order_id = models.Column(models.Integer, models.ForeignKey("order.id"))
    order = models.relationship("Order", backref="orderitem")
    quantity = models.Column(models.Integer)

    def __repr__(self):
        return f"<OrderItem {self.item.title}>"

class Order(FlaskSerializeMixin, models.Model):
    id = models.Column(models.Integer, primary_key=True)
    user_id = models.Column(models.Integer, models.ForeignKey("user.id"))
    created_at = models.Column(models.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Item {self.user.username}>"
