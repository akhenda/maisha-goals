try:
    import unittest2 as unittest
except ImportError:  # Python 2.7
    import unittest
from .test_auth import TestAuth
from .test_users import TestUsers
from .test_endpoints import TestEndpoints
from .test_bucketlists import TestBucketlists
from .test_bucketlist_items import TestBucketlistItems

suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAuth)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestUsers)
suite3 = unittest.TestLoader().loadTestsFromTestCase(TestEndpoints)
suite4 = unittest.TestLoader().loadTestsFromTestCase(TestBucketlists)
suite5 = unittest.TestLoader().loadTestsFromTestCase(TestBucketlistItems)

alltests = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5])
