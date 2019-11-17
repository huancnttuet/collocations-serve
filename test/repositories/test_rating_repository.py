import unittest

from app import db
from app.repositories import RatingRepository
from test.factories import RatingFactory
from test.utilities import BaseTestCaseWithDB


class GetByIDTestCase(BaseTestCaseWithDB):

    def test_return_rating_when_passed_exist_id(self):
        rating = RatingFactory.build()
        db.session.add(rating)
        db.session.commit()

        result = RatingRepository.get_by_id(rating.id)

        self.assertEqual(result, rating)

    def test_return_none_when_passed_non_existing_id(self):
        result = RatingRepository.get_by_id(0)

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
