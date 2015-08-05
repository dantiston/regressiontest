"""
regressiontest

Result

@author T.J. Trimble <trimblet@me.com>
"""

class Result(object):

    def report(self):
        """

        """
        result = []
        result.append("#"*20)
        result.append(self._report())
        result.append("#"*20)
        return "\n".join(result)
    

    def _report(self):
        """
        This method returns a string value
        to be added to the body of the report.
        """
        return ""
        
