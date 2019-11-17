from app.models import Rating


class RatingRepository:
    @staticmethod
    def get_by_id(rating_id):
        """ Get Rating record by id

        :param rating_id: str
        :return: Rating
        """
        return Rating.query.get(rating_id)
