from marshmallow import Schema, fields, validate


class VendorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)


class VendorCreateSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)


class VendorUpdateSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    phone = fields.Str()