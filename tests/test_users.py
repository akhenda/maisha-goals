from tests.test_base import TestBase


class TestUsers(TestBase):
    """ Test users' Buckelists """

    def test_get_users(self):
        res, json = self.client.get('/api/v1/users/')
        self.assertEqual(res.status_code, 200)

    def test_get_user(self):
        """ Test that we can fetch a single user """
        # Get user whose ID is 1
        res1, json1 = self.client.get('/api/v1/users/1')
        self.assertEqual(res1.status_code, 200)
        self.assertEqual('Jack', json1['username'])

        # Get user whose ID is 2
        res2, json2 = self.client.get('/api/v1/users/2')
        self.assertEqual(res2.status_code, 200)
        self.assertEqual('Ronon', json2['username'])

    def test_update_user(self):
        """ Test editing of user information """
        res, json = self.client.post('/auth/register',
                                     data={
                                        'username': 'Jaffa',
                                        'password': '123'
                                     })
        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            json['message'],
            "Your account has been successfuly created"
        )
        location = res.headers['Location']
        res1, json1 = self.client.put(location, data={"password": "1234"})
        self.assertEqual(res1.status_code, 200)
        self.assertTrue(
            json1['message'],
            "User successfuly updated"
        )

    def test_delete_user_account(self):
        """ Test deletion of a user account """
        res, json = self.client.post('/auth/register',
                                     data={
                                        'username': 'Apophis',
                                        'password': 'pass'
                                     })
        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            json['message'],
            "Your account has been successfuly created"
        )
        location = res.headers['Location']
        res1, json1 = self.client.delete(location)
        self.assertEqual(res1.status_code, 200)
        self.assertTrue(
            json1['message'],
            "User successfuly deleted"
        )
