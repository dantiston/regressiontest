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


def getFirst(string):
    return string[0]


# Functions
def run(args):
    tests = expandPattern(args.pattern)
    for test in tests:
        regressiontest.runTest(test)


def create(args):
    filenames = args.filenames
    function = args.function
    for filename in filenames:
        regressiontest.createTest(function, filename)


def update(args):
    tests = expandPattern(args.pattern)
    for test in tests:
        regressiontest.updateTest(test)


def delete(args):
    tests = expandPattern(args.pattern)
    if len(test) > 1:
        print("Deletion command only accepts one fully-specified test at a time.",
              file=sys.stderr)
        sys.exit(1)
    regressiontest.deleteTest(test)


def search(args):
    tests = expandPattern(args.pattern)
    print(", ".join(tests))



# Argument parser
parser = argparse.ArgumentParser(prog=constants.project,
                                 description='Create and run regression tests.')

# Optional commands
parser.add_argument('-v', '--version', action='version', version=" ".join(("%(prog)s", constants.version)))


# Subcommand parser
subparsers = parser.add_subparsers(title="commands",
                                   help='command to execute',
                                   dest='command')
subparsers.required = True # Make at least one of the subparsers required


## Create subparser
parser_create = subparsers.add_parser('c',
                                      aliases=['create'],
                                      help='Create a new regression test')
parser_create.add_argument("function", type=str,
                           help="function to test")
parser_create.add_argument("filenames", type=str, nargs='+',
                           help="filenames to ingest and create new tests from")
parser_create.set_defaults(f=create)


## Run subparser
parser_run = subparsers.add_parser('r',
                                   aliases=['run'],
                                   help='Run the tests matching the specified pattern')
parser_run.add_argument("pattern", type=str,
                        help="pattern matching names of regression tests to run")
parser_run.set_defaults(f=run)


## Update subparser
parser_update = subparsers.add_parser('u',
                                      aliases=['update'],
                                      help='Update the tests matching the specified pattern')
parser_update.add_argument("pattern", type=str,
                           help="pattern matching names of regression tests to update")
parser_update.set_defaults(f=update)


## Delete subparser
parser_delete = subparsers.add_parser('d',
                                      aliases=['delete'],
                                      help='Delete the test specified')
parser_delete.add_argument("name", type=str,
                           help="name of test to delete")
parser_delete.set_defaults(f=delete)


## Search subparser
parser_search = subparsers.add_parser('s',
                                      aliases=['search'],
                                      help='Search for tests matching the pattern')
parser_search.add_argument("pattern", type=str,
                           help="pattern to search for")
parser_search.set_defaults(f=search)


# Execute command
args = parser.parse_args()
args.f(args)
