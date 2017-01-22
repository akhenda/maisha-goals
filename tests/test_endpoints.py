from .test_base import TestBase
from werkzeug.exceptions import Unauthorized, NotFound, MethodNotAllowed
from app.exceptions import ConflictError, ValidationError


class TestEndpoints(TestBase):
    """ Test the API endpoints """

    def test_home_endpoint(self):
        res, json = self.client.get('/api/v1')
        self.assertEqual(res.status_code, 200)

    def test_requests_with_no_token(self):
        """ Test that tokens are required for secured endpoints """
        res1, json1 = self.client.get('/api/v1/bucketlists/',
                                      headers={'Authorization': ''})
        self.assertEqual(res1.status_code, 401)
        self.assertEqual(
            json1['message'],
            "please send your authentication token"
        )

        res2, json2 = self.client.put('/api/v1/bucketlists/1',
                                      data={'name': 'Update BList'},
                                      headers={'Authorization': ''})
        self.assertEqual(res2.status_code, 401)
        self.assertEqual(
            json2['message'],
            "please send your authentication token"
        )

        res3, json3 = self.client.post("/api/v1/bucketlists/2/items/",
                                       data={"title": "Ndoo1",
                                             "description": "Jaza ndoo maji"},
                                       headers={'Authorization': ''})
        self.assertEqual(res3.status_code, 401)
        self.assertIn(
            "please send your authentication token",
            json3["message"]
        )

    def test_requests_with_invalid_tokens(self):
        # with self.assertRaises(Unauthorized):
        res1, json1 = self.client.post('/api/v1/bucketlists/3/items/',
                                       data={'name': 'New BList item'},
                                       headers={
                                            'Authorization': 'inVal1D^TokEN'
                                            })
        self.assertEqual(res1.status_code, 401)
        self.assertEqual(
            json1['message'],
            "please send your authentication token"
        )

        # with self.assertRaises(Unauthorized):
        res2, json2 = self.client.delete('/api/v1/bucketlists/2/items/3',
                                         headers={
                                            'Authorization': 'inVal1D^TokEN'
                                            })
        self.assertEqual(res2.status_code, 401)
        self.assertEqual(
            json2['message'],
            "please send your authentication token"
        )

    def test_invalid_urls(self):
        with self.assertRaises(NotFound):
            res1, json1 = self.client.post('/api/v1/bucketlist/3/items/',
                                           data={'name': 'New BList item'})
            self.assertEqual(res1.status_code, 404)
            self.assertEqual(
                json1['message'],
                "The requested url was not found"
            )
        with self.assertRaises(NotFound):
            res2, json2 = self.client.put('/api/v1/bucketlists//2/items/3',
                                          data={'name': 'New BList item'})
            self.assertEqual(res2.status_code, 404)
            self.assertEqual(
                json2['message'],
                "The requested url was not found"
            )
        with self.assertRaises(NotFound):
            res3, json3 = self.client.get('/api/v1/bucketlists//')
            self.assertEqual(res3.status_code, 404)
            self.assertEqual(json3['message'], 'The requested url was not found')

    def test_invalid_query_parameters(self):
        with self.assertRaises(ValidationError):
            res1, json1 = self.client.get('/api/v1/bucketlists/?limitt=20')
            self.assertEqual(res1.status_code, 400)
            self.assertEqual(
                json1['message'],
                "invalid query parameter"
            )
        with self.assertRaises(ValidationError):
            res2, json2 = self.client.get('/api/v1/bucketlists/?s=blist')
            self.assertEqual(res2.status_code, 400)
            self.assertEqual(
                json2['message'],
                "invalid query parameter"
            )
        with self.assertRaises(ValidationError):
            res3, json3 = self.client.get('/api/v1/bucketlists/?limit=abc')
            self.assertEqual(res3.status_code, 400)
            self.assertIn(
                'limit query parameter only accepts integers',
                json3['message']
            )

    def test_allowed_url_methods(self):
        with self.assertRaises(MethodNotAllowed):
            res1, json1 = self.client.put('/api/v1/bucketlists/3/items/',
                                          data={'name': 'New BList item'})
            self.assertEqual(res1.status_code, 405)
            self.assertEqual(
                json1['message'],
                "The PUT method is not allowed on this endpoint"
            )
        with self.assertRaises(MethodNotAllowed):
            res2, json2 = self.client.post('/api/v1/bucketlists/2/items/3',
                                           data={'name': 'New BList item'})
            self.assertEqual(res2.status_code, 405)
            self.assertEqual(
                json2['message'],
                "The POST method is not allowed on this endpoint"
            )
        with self.assertRaises(MethodNotAllowed):
            res3, json3 = self.client.delete('/api/v1/bucketlists/2/items/')
            self.assertEqual(res3.status_code, 405)
            self.assertIn(
                'The DELETE method is not allowed on this endpoint',
                json3['message']
            )

    def test_malformed_post_and_put_requests(self):
        with self.assertRaises(ValidationError):
            res1, json1 = self.client.post('/api/v1/bucketlists/',
                                           data={'title': 'New BList item'})
            self.assertEqual(res1.status_code, 400)
            self.assertEqual(
                json1['message'],
                "This resource does not have a field named 'title'"
            )
        with self.assertRaises(ValidationError):
            res2, json2 = self.client.put('/api/v1/bucketlists/1',
                                          data={'title': 'Updated BList'})
            self.assertEqual(res2.status_code, 400)
            self.assertEqual(
                json2['message'],
                "This resource does not have a field named 'title'"
            )
        with self.assertRaises(TypeError):
            res3, json3 = self.client.delete('/api/v1/bucketlists',
                                             data={'description': 'dance time'})
            self.assertEqual(res3.status_code, 400)
            self.assertIn(
                'Please provide a name for the bucketlist',
                json3['message']
            )
        with self.assertRaises(TypeError):
            res4, json4 = self.client.delete('/api/v1/bucketlists/2/items/',
                                             data={"nam": "Ndoo3",
                                                   "description": "Maji ya kufua"})
            self.assertEqual(res4.status_code, 400)
            self.assertIn(
                'Please provide a name for the bucketlist item',
                json4['message']
            )
