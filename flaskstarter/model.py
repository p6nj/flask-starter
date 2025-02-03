from peewee import (
    CharField,
    BooleanField,
    TextField,
    DecimalField,
    IntegerField,
    Model,
    Check,
    ForeignKeyField,
)


class Product(Model):
    # id = BigIntegerField(primary_key=True)
    name = CharField()
    in_stock = BooleanField(default=True)
    description = TextField(null=True)
    price = DecimalField(
        max_digits=5, decimal_places=2, constraints=[Check("price > 0")]
    )
    weight = IntegerField(null=True, constraints=[Check("weight > 0")])
    image = CharField()


class ShippingInformation(Model):
    country = CharField()
    address = CharField()
    postal_code = CharField()
    city = CharField()
    province = CharField(max_length=2)


class ProductOrderQuantity(Model):
    # TODO: uncomment line below and move class definition to have multiple products per order (next version)
    # oid = ForeignKeyField(Order, backref='products')
    pid = ForeignKeyField(Product, backref="order_quantities", column_name="id")
    quantity = IntegerField(constraints=[Check("quantity > 0")])


class Order(Model):
    # peewee automatically adds an auto-incrementing id
    product = ForeignKeyField(ProductOrderQuantity)
    email = CharField(null=True)
    credit_card = CharField(null=True)  # TODO: switch type to something more meaningful
    shipping_information = ForeignKeyField(
        ShippingInformation, backref="orders_shipped_there", null=True
    )
    transaction = CharField(null=True)  # TODO: switch type to something more meaningful
    paid = BooleanField(default=False)
