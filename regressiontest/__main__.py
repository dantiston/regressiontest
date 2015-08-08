"""
regressiontest

__main__

CLI for regressiontest module

Many of the CLI methods support wildcard expansion,
termed here "test patterns", such as "*link*" to
find tests with tests with the term "link" somewhere
in them.

Commands:
    (r)un:
        Run the tests specified by the name arguments.
    (c)reate:
        Given a function and a filename pointing to a file
        of newline separated JSON objects, create a test
        entry for each item in the file.
    (u)pdate:
        Update the tests matching the given test pattern.
    (d)elete:
        Delete the test with the specified word. The given
        term must exactly match the specified word.
    (s)earch:
        Search for tests matching the given pattern.
"""

import sys
import argparse

from regressiontest import regressiontest
from regressiontest import constants

# Utilities
def expandPattern(name):
    # Get the names
    # Search the names
    result = []
    result.append(name) # TODO: DELETEME
    return result


# Functions
def run(filenames):
    for filename in filenames:
        regressiontest.runTest(filename)


def create(function, filenames):
    for filename in filenames:
        regressiontest.createTest(function, filename)


def update(filenames):
    for filename in filenames:
        regressiontest.updateTest(filename)


def delete(filename):
    if len(filename) > 1:
        print("Deletion command only accepts one file at a time.",
              file=sys.stderr)
    regressiontest.deleteTest(filename)


def search(filenames):
    print(", ".join(filenames))


functionDict = {
    "r":run,
    "c":create,
    "u":update,
    "d":delete,
    "s":search,
}

# Parse args
parser = argparse.ArgumentParser(prog=constants.project,
                                 description='Create and run regression tests.')
parser.add_argument("command", choices=functionDict.keys(), type=lambda x: x[0],
                    help="command to process: one of {" + ",".join(functionDict.keys()) + "}")
parser.add_argument("pattern", type=str,
                    help="pattern matching names of regression tests to process")

# Optional commands
parser.add_argument('--version', action='version', version="%(prog)s " + constants.version)

args = parser.parse_args()

if args.command not in functionDict:
    parser.print_usage()
    sys.exit(1)

# Execute command
functionDict[args.command](expandPattern(args.pattern))
