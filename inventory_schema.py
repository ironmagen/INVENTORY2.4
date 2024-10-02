from marshmallow import Schema, fields, validate


class InventorySchema(Schema):
    id = fields.Int(dump_only=True)
    item_name = fields.Str(required=True)
    category_id = fields.Int()
    vendor_id = fields.Int()
    price = fields.Decimal(places=2, as_string=True)
    stock = fields.Int()
    units = fields.Str()
    status = fields.Str()
    par = fields.Int()
    order_strike = fields.Int()
    cost_on_hand = fields.Decimal(places=2, as_string=True)


class InventoryCreateSchema(Schema):
    item_name = fields.Str(required=True)
    category_id = fields.Int()
    vendor_id = fields.Int()
    price = fields.Decimal(places=2, as_string=True)
    stock = fields.Int()
    units = fields.Str()
    status = fields.Str()
    par = fields.Int()
    order_strike = fields.Int()
    cost_on_hand = fields.Decimal(places=2, as_string=True)


class InventoryUpdateSchema(Schema):
    item_name = fields.Str()
    category_id = fields.Int()
    vendor_id = fields.Int()
    price = fields.Decimal(places=2, as_string=True)
    stock = fields.Int()
    units = fields.Str()
    status = fields.Str()
    par = fields.Int()
    order_strike = fields.Int()
    cost_on_hand = fields.Decimal(places=2, as_string=True)