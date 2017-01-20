from .test_base import TestBase


class TestBucketlists(TestBase):
    """ Test users' Buckelists """

    def test_add_bucketlist(self):
        res, json = self.client.post('/api/v1/bucketlists/',
                                     data={'name': 'Mars'})
        self.assertEqual(res.status_code, 201)
        self.assertTrue(
            json['message'],
            "Your bucketlist was successfuly created"
        )
        self.assertIn('Mars', json['name'])
        self.assertTrue(json['description'] == '')

    def test_update_bucketlist(self):
        """ Test editing of bucket lists """
        res, json = self.client.put('/api/v1/bucketlists/2',
                                    data={"name": "Ndoo4"})
        self.assertEqual(res.status_code, 200)
        self.assertTrue(
            json['message'],
            "Your bucketlist was successfuly edited"
        )
        self.assertIn('Ndoo4', json['name'])
        self.assertTrue(json['description'] == '')

    def test_delete_bucketlist(self):
        """ Test deletion of a bucketlist """
        res, json = self.client.delete('/api/v1/bucketlists/1')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(
            json['message'],
            "Your bucketlist was successfuly deleted"
        )

    def test_get_bucketlist(self):
        """ Test that we can fetch a specific bucket list """
        # Get bucket list whose ID is 2
        res1, json1 = self.client.get('/api/v1/bucketlists/2')
        self.assertEqual(res1.status_code, 200)
        self.assertIn('Ndoo4', json1['name'])
        self.assertTrue(json1['description'] == '')

        # Get bucket list whose ID is 4
        res2, json2 = self.client.get('/api/v1/bucketlists/4')
        self.assertEqual(res2.status_code, 200)
        self.assertIn('Ndoo4', json2['name'])
        self.assertTrue(json2['description'] == '')

    def test_get_bucketlists(self):
        """ Test that all bucket lists are displayed """
        res, json = self.client.get('/api/v1/bucketlists/')
        self.assertEqual(res.status_code, 200)

    def test_methods_on_invalid_bucketlist(self):
        """
        Tests to cover all invalid bucketlists scenarios
        """
        res1, json1 = self.client.get('/api/v1/bucketlists/233')
        self.assertEqual(res1.status_code, 404)
        self.assertTrue(
            json1['message'],
            "The requested bucketlist does not exist"
        )

        """ Test editing a bucketlists that doesn't exist """
        res2, json2 = self.client.put('/api/v1/bucketlists/221',
                                      data={
                                        "name": "ndoo5",
                                        "description": "no desc"
                                      })
        self.assertEqual(res2.status_code, 404)
        self.assertTrue(
            json['message'],
            "Cannot edit a bucketlist that does not exist"
        )

        """ Test deletion of a bucketlist """
        res3, json3 = self.client.put('/api/v1/bucketlists/221')
        self.assertEqual(res3.status_code, 404)
        self.assertTrue(
            json3['message'],
            "Cannot delete a bucketlist that does not exist"
        )

    def test_operation_on_another_user_bucketlist(self):
        """ Test that users cannot access other users' bucketlists """
        # Attempt to get another user's bucketlist
        res1, json1 = self.client2.get('/api/v1/bucketlists/1')
        self.assertEqual(res1.status_code, 403)
        self.assertTrue(
            json1['message'],
            "You do not have permission to access this resource"
        )

        # Attempt to update another user's bucketlist
        res2, json2 = self.client2.put('/api/v1/bucketlists/1',
                                       data={
                                        "name": "ndoo6",
                                        "description": "desc"
                                       })
        self.assertEqual(res2.status_code, 403)
        self.assertTrue(
            json2['message'],
            "You do not have permission to edit this resource"
        )

        """ Test deletion of another user's bucketlist """
        res3, json3 = self.client2.delete('/api/v1/bucketlists/1')
        self.assertEqual(res3.status_code, 403)
        self.assertTrue(
            json3['message'],
            "You do not have permission to delete this resource"
        )

    def test_add_duplicate_bucketlist(self):
        """ Test creation of a bucketlist with an existing name """
        res, json = self.client.post('/api/v1/bucketlists/',
                                     data={
                                        "name": "Ndoo2"
                                     })
        self.assertEqual(res.status_code, 409)
        self.assertTrue(
            json['message'],
            "You already have a bucketlist with that name"
        )
