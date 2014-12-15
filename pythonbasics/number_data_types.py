""" Shows different data types for data analysis """

from __future__ import division
# In Python 2.7, ratio of two ints was always an int (e.g. 9/5 is 1)
# In Python 3, ratio of two ints converts to a floating point (9/5 is 1.8)
from __future__ import unicode_literals
# Unicode expands from 128 chars to 2^31 chars
# In Python 2.7, need to specify u'unicode string' and Python 3 does by default


def number_example():
    """ Int and Floating Point are the most important scalar data type """

    x = 1  # Integer can range from: -2^31 to 2^31 -1
    print type(x), " is a 32 bit or 64 bit int"
    # <type 'int'>  is a 32 bit or 64 bit int

    x = 1.0  # Float
    print type(x), " is a float"
    # <type 'float'>  is a float

    x = 1j  # Complex
    print type(x), " is a complex"
    # <type 'complex'>  is a complex

    x = long(2)  # Long has no range limitation
    print x  # The trailing L after the number indicates as long
    print type(x), " is a long"
    # <type 'long'>  is a long


if __name__ == '__main__':
    number_example()
