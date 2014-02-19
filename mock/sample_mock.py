# Using mock to replace parts of system under test with mock objects
# Allows monkey patch of methods (i.e. dynamic modifications to code 
#    during runtime)
# Basically, allows you to mimic any other Python class

import mock

# Mock and MagicMock objects create all attributes and methods as you
# access them and store details of how they have been used
# You can configure them, specify return values or limit what attributes are
# available and then make assertions about how they have been used

# Creating a Mock() object then assigning attributes
myMock = mock.Mock(
    greeting = "hey there"
    )
myMock.greeting = "hello world!"
print "myMock's attributes for greeting: ", myMock.greeting

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

# Mocking a Class
class ProductionClass(object):
    def method(self):
        self.something(1,2,3)
    def something(self, a, b, c):
        pass

thing = ProductionClass()
thing.method = mock.MagicMock(return_values=3)
thing.method(1, 2, 3, key='value')

thing.method.assert_called_with(1, 2, 3, key='value')

