from .test_base import TestBase


class TestAuth(TestBase):
    """ Test user registration and login """

    def test_successful_registration(self):
        ''' Test add a user to the DB '''
        res, json = self.client.post('/api/v1/auth/register',
                                     data={'name': 'Rodney'})
        self.assertEqual(res.status_code, 201)
        location = res.headers['Location']
        res, json = self.client.get(location)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(json['name'] == 'Rodney')
        self.assertEqual(
            json['message'],
            "Your account has been successfuly created"
        )

    def test_unsuccessful_registration(self):
        ''' Register a user with a username already in the DB'''
        res, json = self.client.post('/api/v1/auth/register',
                                     data={'name': 'Ronon'})
        self.assertTrue(res.status_code == 409)
        self.assertEqual(
            json['message'],
            "The username has been taken. Try another username"
        )

    def test_successful_login(self):
        ''' Test User login '''
        res, json = self.client.post("/api/v1/auth/login",
                                     data={
                                        'username': 'Jack',
                                        'password': 'test'
                                     })
        self.assertEqual(res.status_code, 200)
        self.assertIn("You have successfully logged in", json['message'])

    def test_unsuccessful_login(self):
        ''' Test User invalid credentials '''
        res, json = self.client.post("/api/v1/auth/login",
                                     data={
                                        'username': 'Jackson',
                                        'password': 'testing'
                                     })
        self.assertEqual(res.status_code, 403)
        self.assertIn("Incorrect username or password", json['message'])
