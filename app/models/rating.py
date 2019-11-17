import uuid

from app import db
from app.models.mixins import BaseMixin


def generate_uuid():
    return str(uuid.uuid4())


class Rating(db.Model, BaseMixin):
    __tablename__ = 'ratings'

    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
