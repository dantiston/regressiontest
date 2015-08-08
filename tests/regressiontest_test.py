"""
RegressionTestTest

@author T.J. Trimble <trimblet@me.com>
"""

import unittest
import json

class RegressionTestTest(unittest.TestCase):

    jsonTestPath = "regressiontests/jsontest.json"


    def setup(self):
        self.testJson = json.load(jsonTestPath)


    def testCreateTests():
        pass


    def testRunTestsAgainstJson():
        #try:
        #    regressiontest.
        pass
