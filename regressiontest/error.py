"""
regressiontest

Error

@author T.J. Trimble <trimblet@me.com>
"""

from result import Result

class Error(Result):


    def __init__(self, expected, error):
        self.expected = expected
        self.error = error
        

    def _report(self):
        """
        This method returns a string value
        to be added to the body of the report.
        """
        return "\n".join(("Error:",
                          self.error,
                          self.expected))
        
