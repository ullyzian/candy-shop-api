from datetime import datetime
from api import db

tags_table = db.Table(
    "tag_associations",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
    db.Column("item_id", db.Integer, db.ForeignKey("item.id")),
)


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
    tags = db.relationship("Tag", secondary=tags_table)

    def __init__(self, *args):
        self.name = args[0]
        self.price = args[1]
        self.description = args[2]
        self.img = args[3]
        self.tags = args[4]


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
