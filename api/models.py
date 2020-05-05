from datetime import datetime
from api import db

class TagItemRel(db.Model):
    rel_id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)

    def __init__(self, tag_id, item_id):
        self.tag_id = tag_id
        self.item_id = item_id


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, label):
        self.label = label


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    img = db.Column(db.Text)
    order_item = db.relationship("OrderItem", uselist=False, backref="item")

    def __init__(self, *args):
        self.name = args[0]
        self.price = args[1]
        self.description = args[2]
        self.img = args[3]


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
        return f"<OrderItem {self.order_id}>"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __init__(self, email):
        self.email = email;
    
    def __repr__(self):
        return f"<Item {self.user.username}>"
