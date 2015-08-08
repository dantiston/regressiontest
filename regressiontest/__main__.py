"""
regressiontest

__main__

CLI for regressiontest module
"""

import sys
import argparse

from regressiontest import regressiontest

print(dir(regressiontest))

# Parse args
parser = argparse.ArgumentParser(description='Create and run regression tests.')
parser.add_argument("filenames", type=str, nargs="+",
                    help="filename(s) storing regression tests to process")


args = parser.parse_args()

# Run tests
for filename in args.filenames:
    regressiontest.runTest(filename)
