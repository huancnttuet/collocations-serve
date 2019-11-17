import uuid

from app import db
from app.models.mixins import BaseMixin


class Client(db.Model, BaseMixin):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
