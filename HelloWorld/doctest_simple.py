"""
*  Testing doctest using $python -m doctest -v doctest_simple.py
*  doctest tests source code by running examples embedded in the documentation
   and verifies that they produce the expected results.
*  Steps: 
       1.)  Parses the help text to find examples
       2.)  Runs the test cases
       3.)  Compares output text against expected values
"""

def my_function(a,b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b

