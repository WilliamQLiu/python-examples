"""
*  Testing doctest using $python -m doctest -v doctest_simple_with_docs.py
*  This version has extra strings more human readable test scenarios
*  doctest tests source code by running examples embedded in the documentation
   and verifies that they produce the expected results.
*  Steps: 
       1.)  Parses the help text to find examples
       2.)  Runs the test cases
       3.)  Compares output text against expected values
"""

def my_function(a,b):
    """
    This function returns a * b.

    Works with numbers (see how this text doesn't interfere with testing):
    >>> my_function(2, 3)
    6

    and strings: (see how this text doesn't interfere with testing)
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b


"""Output is:
    1 items had no tests:
        doctest_simple_with_docs
    1 items passed all tests:
        2 tests in doctest_simple_with_docs.my_function
    2 tests in 2 items.
    2 passed and 0 failed.
    Test passed
"""