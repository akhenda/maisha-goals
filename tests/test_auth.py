from .test_base import TestBase
from base64 import b64encode


class TestAuth(TestBase):
    """ Test user registration and login """

    def test_successful_registration(self):
        ''' Test successful user registration '''
        res, json = self.client.post('/auth/register',
                                     data={
                                        'username': 'Rodney',
                                        'password': '123'
                                     })
        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            json['message'],
            "Your account has been successfuly created"
        )
        location = res.headers['Location']
        res1, json1 = self.client.get(location)
        self.assertEqual(res1.status_code, 200)
        self.assertTrue(json1['username'] == 'Rodney')
        self.assertEqual(json1['self_url'], location)

    def test_unsuccessful_registration(self):
        ''' Register a user with a username already in the DB'''
        res, json = self.client.post('/auth/register',
                                     data={
                                        'username': 'Ronon',
                                        'password': '123'
                                     })
        self.assertTrue(res.status_code == 409)
        self.assertEqual(
            json['message'],
            "that username is taken"
        )

    def test_successful_login(self):
        ''' Test successful user login '''
        auth_header = 'Basic ' + b64encode(('Jack:test')
                                           .encode('utf-8')).decode('utf-8')
        res, json = self.client.get('/auth/login',
                                    headers={'Authorization': auth_header})
        self.assertEqual(res.status_code, 200)
        self.assertIn('token', json)

    def test_unsuccessful_login(self):
        ''' Test unsuccessful user login with invalid credentials '''
        auth_header = 'Basic ' + b64encode(('Jack:testing')
                                           .encode('utf-8')).decode('utf-8')
        res, json = self.client.get('/auth/login',
                                    headers={'Authorization': auth_header})
        self.assertEqual(res.status_code, 401)
        self.assertIn("please authenticate", json['message'])
