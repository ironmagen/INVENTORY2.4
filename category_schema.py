from marshmallow import Schema, fields, validate


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()


class CategoryCreateSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()


class CategoryUpdateSchema(Schema):
    name = fields.Str()
    description = fields.Str()