from app import db
from app.models.mixins import BaseMixin

class UploadFile(db.Model, BaseMixin):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
