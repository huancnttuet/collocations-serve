from app import db
from app.extensions.exceptions.rating import RatingNotSaveException, RatingNotFoundException
from app.models import Rating
from app.repositories import RatingRepository


class RatingService:
    @staticmethod
    def create_rating(data):
        new_rating = Rating(**data)
        db.session.add(new_rating)
        db.session.commit()

        if new_rating is None:
            raise RatingNotSaveException
        return new_rating

    @staticmethod
    def get_by_id(rating_id):
        rating = RatingRepository.get_by_id(rating_id)

        if rating is None:
            raise RatingNotFoundException

        return rating
