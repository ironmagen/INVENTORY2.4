from marshmallow import Schema, fields
from .delivery_item_schema import DeliveryItemSchema

class DeliverySchema(Schema):
    class Meta:
        fields = (
            'id',
            'date',
            'order_id',
            'vendor_name',
            'delivery_items'
        )
    
    delivery_items = fields.List(fields.Nested(DeliveryItemSchema))