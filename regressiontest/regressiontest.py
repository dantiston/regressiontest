"""
regressiontest

RegressionTest

This module provides RegressionTest, a class
for saving, loading, and comparing the state
of code. This module is built upon the json
library, and relies on pickle API implementations.

Logs are stored at tests/regressiontests/logs/

@author T.J. Trimble <trimblet@me.com>
"""

import json
from regressiontest import constants

def createTestFromObjectWithList(filename, data, function, name):
    """
    Run the specified function on the specified data,
    saving the results in JSON format to the specified
    filename.

    This method takes a function which returns an
    object, applies to the specified iterable, and
    saves the result.
    """
    results = (function(item).dumps() for item in data)
    _createTest(filename, data, results, function, name, constants.objectName)


def createTestFromObjectFromItem(filename, item, function, name):
    """
    Run the specified function on the specified data,
    saving the results in JSON format to the specified
    filename.

    This method takes a function which returns an
    object, applies it to the specified input,
    and saves the result.
    """
    createTestFromObjectWithList(filename, (item,), function, name, constants.objectName)


def createTestFromJsonWithList(filename, data, function, name):
    """
    Run the specified function on the specified data,
    saving the results in JSON format to the specified
    filename.

    This method takes a function which returns a JSON
    Object or JSON Array, applies it to the specified
    input, and saves the result.
    """
    results = (function(item) for item in data)
    _createTest(filename, data, results, function, name, constants.jsonName)


def createTestFromJsonFromItem(filename, item, function, name):
    """
    Run the specified function on the specified data,
    saving the results in JSON format to the specified
    filename.

    This method takes a function which returns a JSON
    Object or JSON Array, applies it to the specified
    input, and saves the result.
    """
    createTestFromObjectWithList(filename, (item,), function, name, constants.jsonName)


def _createTest(filename, data, generator, function, name, typeName):
    """
    Given a filename, generator, and function, run
    the function and save the results to file.

    The generator should return a sequence of JSON
    Objects or JSON Arrays.
    """
    try:
        results = json.loads(str(list(generator)))
    except Exception as e:
        raise RuntimeError("Running function \"{}\" on data failed with Exception {} \ndata: {}".format(function,e,data))
    output = {
        constants.inputKey: data,
        constants.expectedKey: results,
        constants.nameKey: name,
        constants.typeKey: typeName
    }
    try:
        with open(filename, 'a') as fd:
            fd.write(output)
    except FileNotFoundError as e:
        raise e



def runTest(filename):
    # Load test

    # Run the appropriate method depending if test is JSON or Object test

    pass



def runTestAgainstObject(self, filename, function, loader):
    """
    Load the JSON data from the given filename,
    run the given function on the input data,
    and compare the result of the function
    to the object representation built by the
    loader reading the expected JSON.
    """
    data = json.load(filename)
    results = []
    for json in data:
        results.add(_runtest(json, function, loader(json[constants.expectedKey])))

    for result in results:
        print(result.report())


def runTestAgainstJson(filename, function):
    """
    Load the JSON data from the given filename,
    run the given function on the input data,
    and compare the result of the function
    to the JSON stored in the file.
    """
    data = json.load(filename)
    results = []
    for json in data:
        results.add(_runtest(json, function, json[constants.expectedKey]))

    for result in results:
        print(result.report())


def _runtest(json, function, expected):
    try:
        result = function(json[constants.inputKey])
        if result == expected:
            print(constants.success, end='')
            return Success()
        else:
            print(constants.failure, end='')
            return Failure(expected, result)
    except Exception as e:
        print(constants.error, end='')
        return Error(expected, e)


def deleteTest(name):
    # Open file

    # Load file

    # Remove name
    data = (item for item in data if item[regressiontest.nameKey] != name)
    # Write file
