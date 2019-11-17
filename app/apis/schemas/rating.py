from .base import BaseResponseSchema
from marshmallow.fields import Integer
from marshmallow import Schema, validate


class RatingCreateSchema(Schema):
    product_id = Integer(required=True)
    user_id = Integer(required=True)
    client_id = Integer(required=True)
    rating = Integer(required=True)


class RatingResponseSchema(BaseResponseSchema):
    product_id = Integer(required=True)
    user_id = Integer(required=True)
    client_id = Integer(required=True)
    rating = Integer(required=True)
