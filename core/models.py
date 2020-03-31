from core import db as models


class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(60), index=True, unique=True)
    email = models.Column(models.String(120), index=True, unique=True)
    password_hash = models.Column(models.String(128))
    order_item = models.relationship('OrderItem', )


class Item(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String(50))
    price = models.Column(models.Integer)
    description = models.Column(models.Text)

    def __repr__(self):
        return f"<Item {self.title}>"


class OrderItem(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    user_id = models.Column(models.Integer, models.ForeignKey('user.id'))
