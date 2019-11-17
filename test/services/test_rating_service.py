import unittest
from unittest.mock import patch

from app.extensions.exceptions.rating import RatingNotFoundException
from app.services import RatingService
from test.factories import RatingFactory
from test.utilities import BaseTestCase


class GetByIdTestCase(BaseTestCase):
    @patch('app.repositories.RatingRepository.get_by_id')
    def test_return_correct_rating(self, mock_get_by_id):
        rating = RatingFactory.build()
        mock_get_by_id.return_value = rating

        result = RatingService.get_by_id(rating.id)

        self.assertEqual(result, rating)
        mock_get_by_id.assert_called_once()

    @patch('app.repositories.RatingRepository.get_by_id')
    def test_raise_exception_when_passed_incorrect_id(self, mock_get_by_id):
        mock_get_by_id.return_value = None

        with self.assertRaises(RatingNotFoundException):
            RatingService.get_by_id(1)
            mock_get_by_id.assert_called_once()


if __name__ == '__main__':
    unittest.main()
