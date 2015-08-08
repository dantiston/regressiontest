"""
regressiontest

Success

@author T.J. Trimble <trimblet@me.com>
"""

from result import Result

class Success(Result):


    def _report(self):
        """
        This method returns a string value
        to be added to the body of the report.
        """
        return ""
