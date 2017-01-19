import unittest
from .test_auth import TestAuth
from .test_endpoints import TestEndpoints
from .test_bucketlists import TestBucketlists
from .test_bucketlist_items import TestBucketlistItems

suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAuth)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestEndpoints)
suite3 = unittest.TestLoader().loadTestsFromTestCase(TestBucketlists)
suite4 = unittest.TestLoader().loadTestsFromTestCase(TestBucketlistItems)

alltests = unittest.TestSuite([suite1, suite2, suite3, suite4])
