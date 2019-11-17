from marshmallow.fields import Integer, String

from app.apis.schemas import BaseResponseSchema


class IdOnlySchema(BaseResponseSchema):
    id = String(required=True)
