from .test_base import TestBase


class TestEndpoints(TestBase):
    """ Test the API endpoints """

    def test_requests_with_no_token(self):
        res1, json1 = self.client.get('/api/v1/bucketlists/',
                                      headers={'Authorization': ''})
        self.assertTrue(res1.status_code == 403)
        self.assertTrue(
            json1['message'],
            "You are forbidden to view this resource"
        )
        res2, json2 = self.client.put('/api/v1/bucketlists/1',
                                      data={'name': 'Update BList'},
                                      headers={'Authorization': ''})
        self.assertTrue(res2.status_code == 403)
        self.assertTrue(
            json2['message'],
            "You are forbidden to view this resource"
        )

    def test_requests_with_invalid_tokens(self):
        res1, json1 = self.client.post('/api/v1/bucketlists/3/items/',
                                       data={'name': 'New BList item'},
                                       headers={
                                            'Authorization': 'inVal1D^TokEN'
                                            })
        self.assertTrue(res1.status_code == 403)
        self.assertTrue(
            json1['message'],
            "You are forbidden to view this resource"
        )
        res2, json2 = self.client.delete('/api/v1/bucketlists/2/items/3',
                                         data={'name': 'New BList item'},
                                         headers={
                                            'Authorization': 'inVal1D^TokEN'
                                            })
        self.assertTrue(res2.status_code == 403)
        self.assertTrue(
            json2['message'],
            "You are forbidden to view this resource"
        )

    def test_invalid_urls(self):
        res1, json1 = self.client.post('/api/v1/bucketlist/3/items/',
                                       data={'name': 'New BList item'})
        self.assertTrue(res1.status_code == 404)
        self.assertTrue(
            json1['message'],
            "Resource not found"
        )
        res2, json2 = self.client.put('/api/v1/bucketlists//2/items/3',
                                      data={'name': 'New BList item'})
        self.assertTrue(res2.status_code == 404)
        self.assertTrue(
            json2['message'],
            "Resource not found"
        )

    def test_invalid_query_parameters(self):
        res1, json1 = self.client.get('/api/v1/bucketlists?limitt=20')
        self.assertTrue(res1.status_code == 400)
        self.assertTrue(
            json1['message'],
            "Invalid query parameter"
        )
        res2, json2 = self.client.put('/api/v1/bucketlists?s=blist',
                                      data={'name': 'Update BList'})
        self.assertTrue(res2.status_code == 400)
        self.assertTrue(
            json2['message'],
            "Invalid query parameter"
        )

    def test_allowed_url_methods(self):
        res1, json1 = self.client.put('/api/v1/bucketlists/3/items/',
                                      data={'name': 'New BList item'})
        self.assertTrue(res1.status_code == 405)
        self.assertTrue(
            json1['message'],
            "The method is not supported"
        )
        res2, json2 = self.client.post('/api/v1/bucketlists/2/items/3',
                                       data={'name': 'New BList item'})
        self.assertTrue(res2.status_code == 405)
        self.assertTrue(
            json2['message'],
            "he method is not supported"
        )

    def test_malformed_post_and_put_requests(self):
        res1, json1 = self.client.post('/api/v1/bucketlists/',
                                       data={'title': 'New BList item'})
        self.assertTrue(res1.status_code == 400)
        self.assertTrue(
            json1['message'],
            "This resource does not have a field named 'title'"
        )
        res2, json2 = self.client.put('/api/v1/bucketlists/1',
                                      data={'title': 'Updated BList'})
        self.assertTrue(res2.status_code == 400)
        self.assertTrue(
            json2['message'],
            "This resource does not have a field named 'title'"
        )
