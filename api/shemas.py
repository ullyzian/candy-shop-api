from api import ma
from api.models import Item, OrderItem, Order, Tag, User


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag


class ItemSchema(ma.SQLAlchemyAutoSchema):
    tags = ma.Nested(TagSchema, many=True)

    class Meta:
        model = Item


class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem
        include_fk = True


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    orders = ma.Nested(OrderSchema, many=True)

    class Meta:
        model = User


# Init shemas

# User

user_schema = UserSchema()

# Item
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

# OrderItem
orderitem_schema = OrderItemSchema()
orderitems_schema = OrderItemSchema(many=True)

# Order
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
