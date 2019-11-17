import json

from app import db
from app.extensions.api_codes import APICode
from test.factories import ClientFactory
from test.utilities.base_test_cases import BaseTestCaseWithClient


class GetClientByIdTestCase(BaseTestCaseWithClient):
    @classmethod
    def setUpClass(cls):
        super(GetClientByIdTestCase, cls).setUpClass()
        clients = ClientFactory.build_batch(10)

        db.session.bulk_save_objects(clients)
        db.session.commit()

    def test_return_correct_client(self):
        response = self.client.get('/clients/1')
        body = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(body.get("code"), APICode.SUCCESS_GET_CLIENT)
        self.assertEqual(body.get("result").get("id"), "1")

    def test_return_not_found_client(self):
        response = self.client.get('/clients/11')
        body = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(body.get("code"), APICode.CLIENT_NOT_FOUND)
