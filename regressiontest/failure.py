"""
regressiontest

Failure

@author T.J. Trimble <trimblet@me.com>
"""

from result import Result

class Failure(Result):
    

    def __init__(self, expected, result):
        self.expected = expected
        self.result = result
        
    
    def _report(self):
        """
        This method returns a string value
        to be added to the body of the report.
        """
        return "\n".join(("Failure:",
                          "".join(("Expected: \'", self.expected, "\"")),
                          "".join(("Result: \'", self.result, "\""))))
