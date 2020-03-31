from core import db as models


class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(60), index=True, unique=True)
    email = models.Column(models.String(120), index=True, unique=True)
    password_hash = models.Column(models.String(128))
    order_item = models.relationship("OrderItem", backref="author", lazy="dynamic")
    order = models.relationship("Order", backref="author", lazy="dynamic")


    def __repr__(self):
        return f"User {self.username}"


class Item(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String(50))
    price = models.Column(models.Float)
    description = models.Column(models.Text)
    order_item = models.relationship("OrderItem", uselist=False, back_populates="item")

    def __repr__(self):
        return f"<Item {self.title}>"


class OrderItem(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    item_id = models.Column(models.Integer, models.ForeignKey("item.id"))
    # back reference one to one relation to "Item"
    item = models.relationship("Item", back_populates="orderitem")
    user_id = models.Column(models.Integer, models.ForeignKey("user.id"))
    quantity = models.Column(models.Integer)


class Order(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    user_id = models.Column(models.Integer, models.ForeignKey("user.id"))
