"""Showing how to test with doctest's .testfile() using an outside file"""

import doctest

if __name__ == '__main__' :
    doctest.testfile( 'doctest_in_help.rst')