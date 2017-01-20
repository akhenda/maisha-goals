from unittest import TestCase
from base64 import b64encode
import json
from urllib.parse import urlsplit, urlunsplit
from app import create_app, db
from app.models import User, Bucketlist, BucketlistItem


class TestClient():
    ''' This is a Class that wraps the Flask's Test Client and provides API
        friendly features

        Create our custom API Client that extends Flask's client
        One problem that the Flask API Client has is that it is generic, it's
        designed to work with traditional web applications as well as APIs so
        there are a number of things that need to be specified e.g. if you want
        to send a request for an API, you will have to tell it that you want
        JSON data in and out, that you want to authenticate and it gets
        troublesome to have to do that everytime we need to send a request in
        a test. SO we will create a wrapper for Flask's test client and use
        that instead.
    '''
    def __init__(self, app, username, password):
        self.app = app
        self.auth = 'Basic ' + b64encode((username + ':' + password)
                                         .encode('utf-8')).decode('utf-8')

    def send(self, url, method='GET', data=None, headers={}):
        ''' This our generic send fucntion that sends all the requests
            For testing, URLs just need to have the path and query string
            and so we will remove the 'scheme' and 'host' as shown below.
        '''
        url_parsed = urlsplit(url)
        url = urlunsplit(('', '', url_parsed.path, url_parsed.query,
                          url_parsed.fragment))

        # Append the authentication headers to all requests
        headers = headers.copy()
        if not headers['Authorization']:
            headers['Authorization'] = self.auth
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'

        # Convert JSON data to a string
        if data:
            data = json.dumps(data)

        # Send request to the test client and return the response
        with self.app.test_request_context(url, method=method, data=data,
                                           headers=headers):
            rv = self.app.preprocess_request()
            if rv is None:
                rv = self.app.dispatch_request()
            rv = self.app.make_response(rv)
            rv = self.app.process_response(rv)
            return rv, json.loads(rv.data.decode('utf-8'))

    def get(self, url, headers={}):
        return self.send(url, 'GET', headers=headers)

    def post(self, url, data, headers={}):
        return self.send(url, 'POST', data, headers=headers)

    def put(self, url, data, headers={}):
        return self.send(url, 'PUT', data, headers=headers)

    def delete(self, url, headers={}):
        return self.send(url, 'DELETE', headers=headers)


class TestBase(TestCase):
    """ Super class setUp and tearDown for all the test cases """
    default_username = 'Jack'
    default_password = 'test'

    def setUp(self):
        """ Create a test database and set up the test client """
        self.app = create_app('testing')
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.drop_all()
        db.create_all()
        u = User(username=self.default_username)
        u.set_password(self.default_password)
        b1 = Bucketlist(name="World Domination",
                        description="Conquer the world by going back in time",
                        created_by=1)
        b2 = Bucketlist(name="Dragon Balls",
                        description="Find all 7 Dragon Balls",
                        created_by=1)
        i1 = BucketlistItem(name="Build a Time Machine",
                            description="Pay Neil deGrasse a visit",
                            created_by=1,
                            bucketlist_id=1)
        i2 = BucketlistItem(name="Dragon Ball Detector",
                            description="Borrow the Dragon Ball Radar from Bulma",
                            created_by=1,
                            bucketlist_id=2)
        db.session.add(u)
        db.session.add(b1)
        db.session.add(b2)
        db.session.add(i1)
        db.session.add(i2)
        db.session.commit()
        self.client = TestClient(self.app, u.generate_auth_token(), '')

    def tearDown(self):
        """ Destroy the test database and release the app context """
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
