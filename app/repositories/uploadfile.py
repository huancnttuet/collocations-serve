from app.models import UploadFile


class UploadFileRepository:
    @staticmethod
    def get_by_id(file_id):
        """ Get Rating record by id

        :param rating_id: str
        :return: Rating
        """
        return UploadFile.query.get(file_id)
