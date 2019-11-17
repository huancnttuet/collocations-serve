from unittest import TestCase

from app import create_app, db


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('test')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()


class BaseTestCaseWithDB(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseTestCaseWithDB, cls).setUpClass()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
        super(BaseTestCaseWithDB, cls).tearDownClass()

    def tearDown(self):
        db.session.remove()


class BaseTestCaseWithClient(BaseTestCaseWithDB):
    def setUp(self):
        self.client = self.__class__.app.test_client()
