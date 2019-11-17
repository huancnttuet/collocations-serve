from .base import BaseResponseSchema
from marshmallow.fields import Integer, String
from marshmallow import Schema


class ClientCreateSchema(Schema):
    name = String(required=True)
    active = Integer(required=True)


class ClientResponseSchema(BaseResponseSchema):
    name = String(required=True)
    active = Integer(required=True)
