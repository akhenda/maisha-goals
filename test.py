import unittest
import coverage
from tests import alltests


COV = coverage.coverage(branch=True, include='app/*')
COV.start()

unittest.TextTestRunner(verbosity=2).run(alltests)

COV.stop()
COV.report()
