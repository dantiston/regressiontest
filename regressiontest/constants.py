"""
regressiontest

Constants

Constants for use in regressiontest core module

@author T.J. Trimble <trimblet@me.com>
"""


class MetaConstants(type):
    """
    Meta-class to make read-only Constants
    """

    @property
    def project(cls):
        return cls.__project__

    @property
    def version(cls):
        return cls.__version__

    @property
    def nameKey(cls):
        return cls._nameKey

    @property
    def inputKey(cls):
        return cls._inputKey

    @property
    def expectedKey(cls):
        return cls._expectedKey

    @property
    def typeKey(cls):
        return cls._typeKey

    @property
    def objectName(cls):
        return cls._objectName

    @property
    def objectName(cls):
        return cls._jsonName

    @property
    def success(cls):
        return cls._success

    @property
    def failure(cls):
        return cls._failure

    @property
    def error(cls):
        return cls._error



class Constants(metaclass=MetaConstants):
    """
    Constants stores a collection of unmutable strings and other objects
    for consumption by other classes
    """

    __project__ = 'regressiontest'
    __version__ = '0.1'

    _nameKey = 'Name'
    _inputKey = 'Input'
    _expectedKey = 'Expected'
    _typeKey = 'Type'

    _objectName = 'ObjectTest'
    _jsonName = 'JsonTest'

    _success = "."
    _failure = "F"
    _error = "E"
