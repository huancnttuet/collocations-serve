from .base import BaseResponseSchema
from marshmallow.fields import Integer, String
from marshmallow import Schema, validate


class UploadFileCreateSchema(Schema):
    data = String(required=True)


class UploadFileResponseSchema(BaseResponseSchema):
    data = String(required=True)