from marshmallow import Schema, fields

class DeliveryItemSchema(Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'delivery_id',
            'inventory_id',
            'quantity'
        )