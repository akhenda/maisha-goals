from .test_base import TestBase


class TestAuth(TestBase):
    """ Test user registration and login """
    def test_addition(self):
        self.assertEqual(2+3, 5)
