from api import ma
from api.models import Item, OrderItem, Order


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item


class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem
        include_fk = True


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order


# Init shemas

# Item
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

# OrderItem
orderitem_schema = OrderItemSchema()
orderitems_schema = OrderItemSchema(many=True)

# Order
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
