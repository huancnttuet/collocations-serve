from app import db
from app.extensions.exceptions.rating import RatingNotSaveException, RatingNotFoundException
from app.models import UploadFile
from app.repositories import UploadFileRepository


class UploadFileService:
    @staticmethod
    def create_file(data):
        new_file = UploadFile(**data)
        db.session.add(new_file)
        db.session.commit()

        if new_file is None:
            raise RatingNotSaveException
        return new_file

    @staticmethod
    def get_by_id(file_id):
        file = UploadFileRepository.get_by_id(file_id)

        if file is None:
            raise RatingNotFoundException

        return file
