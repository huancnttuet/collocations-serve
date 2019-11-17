import json

from app import db
from app.extensions.api_codes import APICode
from test.factories import RatingFactory
from test.utilities.base_test_cases import BaseTestCaseWithClient


class GetRatingByIdTestCase(BaseTestCaseWithClient):
    @classmethod
    def setUpClass(cls):
        super(GetRatingByIdTestCase, cls).setUpClass()
        ratings = RatingFactory.build_batch(10)

        db.session.bulk_save_objects(ratings)
        db.session.commit()

    def test_return_not_found_rating(self):
        response = self.client.get('/ratings/11')
        body = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(body.get("code"), APICode.RATING_NOT_FOUND)
