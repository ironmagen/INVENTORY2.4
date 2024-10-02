from marshmallow import Schema, fields, validate


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    inventory_id = fields.Int(required=True)
    order_date = fields.Date(required=True)
    quantity = fields.Int(required=True)
    total_cost = fields.Decimal(places=2, as_string=True)


class OrderCreateSchema(Schema):
    inventory_id = fields.Int(required=True)
    order_date = fields.Date(required=True)
    quantity = fields.Int(required=True)
    total_cost = fields.Decimal(places=2, as_string=True)


class OrderUpdateSchema(Schema):
    inventory_id = fields.Int()
    order_date = fields.Date()
    quantity = fields.Int()
    total_cost = fields.Decimal(places=2, as_string=True)