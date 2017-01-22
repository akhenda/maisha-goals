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
            self.client.post('/api/v1/bucketlist/3/items/',
                             data={'name': 'New BList item'})
        with self.assertRaises(NotFound):
            self.client.put('/api/v1/bucketlists//2/items/3',
                            data={'name': 'New BList item'})
        with self.assertRaises(NotFound):
            self.client.get('/api/v1/bucketlists//')

    def test_invalid_query_parameters(self):
        with self.assertRaises(ValidationError):
            self.client.get('/api/v1/bucketlists/?limitt=20')
        with self.assertRaises(ValidationError):
            self.client.get('/api/v1/bucketlists/?s=blist')
        with self.assertRaises(ValidationError):
            self.client.get('/api/v1/bucketlists/?limit=abc')

    def test_allowed_url_methods(self):
        with self.assertRaises(MethodNotAllowed):
            self.client.put('/api/v1/bucketlists/3/items/',
                            data={'name': 'New BList item'})
        with self.assertRaises(MethodNotAllowed):
            self.client.post('/api/v1/bucketlists/2/items/3',
                             data={'name': 'New BList item'})
        with self.assertRaises(MethodNotAllowed):
            self.client.delete('/api/v1/bucketlists/2/items/')

    def test_malformed_post_and_put_requests(self):
        with self.assertRaises(ValidationError):
            self.client.post('/api/v1/bucketlists/',
                             data={'title': 'New BList item'})
        with self.assertRaises(ValidationError):
            self.client.put('/api/v1/bucketlists/1',
                            data={'title': 'Updated BList'})
        with self.assertRaises(TypeError):
            self.client.delete('/api/v1/bucketlists',
                               data={'description': 'dance time'})
        with self.assertRaises(TypeError):
            self.client.delete('/api/v1/bucketlists/2/items/',
                               data={"nam": "Ndoo3",
                                     "description": "Maji ya kufua"})
