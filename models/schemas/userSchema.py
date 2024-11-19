from marshmallow import fields
from schema import ma

class UserSchema(ma.Schema):
    id = fields.Integer(required=False)
    username = fields.String(required=True)
    password = fields.String(required=True)
    customer = fields.Nested('CustomerSchema')

user_schema = UserSchema()
users_schema = UserSchema(many=True)