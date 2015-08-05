"""
regressiontest

RegressionTest

This module provides RegressionTest, a class
for saving, loading, and comparing the state
of code. This module is built upon the json
library, and relies on pickle API implementations.

@author T.J. Trimble <trimblet@me.com>
"""

import json

class RegressionTest(object):
    """
    RegressionTest

    This class provides methods for saving, loading and
    comparing the state of code.
    """

    input_key = 'Input'
    expected_key = 'Expected'

    success = "."
    failure = "F"
    error = "E"

    
    def createtest(self, filename, data, function):
        """
        
        """
        try:
            output = function(data)
        except Exception e:
            raise RuntimeError("Running function \"{}\" on data failed with Exception {} \ndata: {}".format(function,e,data))
        try:
            with open(filename, 'w') as fd:
                fd.write(output)
        except FileNotFoundError e:
            raise e

        

    def runtest(self, filename, function):
        """
        Load the JSON data from the given filename,
        run the given function on the input data,
        and compare it to the expected output.
        """
        data = json.load(filename)
        failures = []
        for json in data:
            try:
                expected = json[RegressionRest.expected_key]
                result = function(json[RegressionTest.input_key])
                if result == expected:
                    print(RegressionTest.success, end='')
                else:
                    print(RegressionTest.failure, end='')
                    failures.add(Failure(expected, result))
            except Exception e:
                print(RegressionTest.error, end='')
                failures.add(Error(expected, e))

        # Report failures
        for failure in failures:
            print(failure.report())
            
        

    def _loadtest(self, json):
        """
        Load the given JSON data.
        The JSON data must be a JSON Array, where
        each item is a JSON Object with two keys:

            "Input"
            "Expected"
        """
        pass        

    

