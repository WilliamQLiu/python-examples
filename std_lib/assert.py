"""
    https://wiki.python.org/moin/UsingAssertionsEffectively
    Asserts are good for debugging, helps do internal self-checks
"""

from types import *  # for asserting types

class Person:
    ''' Simple class to show assertions '''

    def __init__(self, age, color):
        self._myage = age
        self._mycolor = color

    def check_types(self):
        assert type(self._myage) is IntType, "Error - myage is not an integer, instead it is %r" % self._myage
        assert type(self._mycolor) is StringType, "Error - mycolor is not a string, instead it is %r" % self._mycolor



if __name__ == '__main__':

    # Will Pass
    Will = Person(10, "Hello")
    Will.check_types()

    # Will Fail on int
    Laura = Person("20", "Hi")
    Laura.check_types()

    # Will Fail on string
    Billy = Person(30, 40)
    Billy.check_types()