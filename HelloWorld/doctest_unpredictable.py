"""
*  Testing doctest using $python -m doctest -v doctest_unpredictable.py
*  This version ignores specific parts (in this example, the memory address of the object)
*  Handle unpredictable by using #doctest: +ELLIPSIS
*  doctest tests source code by running examples embedded in the documentation
   and verifies that they produce the expected results.
*  Steps: 
       1.)  Parses the help text to find examples
       2.)  Runs the test cases
       3.)  Compares output text against expected values
"""

class MyClass (object):
	pass

def unpredictable(obj):
	"""Returns a new list containing obj.

	>>> unpredictable(MyClass()) #doctest: +ELLIPSIS
	[<doctest_unpredictable.MyClass object at 0x...>]
	"""
	return [obj]

""" Output is:
    Trying:
        unpredictable(MyClass()) #doctest: +ELLIPSIS
    Expecting:
        [<doctest_unpredictable.MyClass object at Ox...>]
    ok
    2 items had no tests:
        doctest_unpredictable
        doctest_unpredictable.MyClass
    1 item passed all tests:
        1 tests in doctest_unpredictable.unpredictable
    1 tests in 3 items.
    1 passed and 0 failed.
    Test passed.
"""