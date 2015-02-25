"""
    Summary:
    Use mock to mimic/ replace parts of Python with mock objects (for testing)
    An example is say we want to test 'Post to Facebook', but don't actually
    want the code to execute and post to Facebook.  Mock fixes this by allowing
    monkey patch of methods (i.e. dynamic modifications to code during runtime)
    Mock is based on an 'action > assertion' pattern used by mocking frameworks

    There's two main ways of using mock; as a patch() decorator and as classes

    1) @mock.patch.someobject decorator mocks instance methods & properties
    * When mocking with multiple decorators, remember that order is important
    * Work backwards, e.g.
        @mock.patch('mymodule.sys')
        @mock.patch('mymodule.os')
        def test_something(self, mock_os, mock_sys):
            pass
    * Executes in this order: patch_sys(patch_os(test_something)

    2) mock.Mock and mock.MagicMock classes
    Mock and MagicMock objects create all attributes and methods as you
    access them and store details of how they have been used.  You can
    configure them, specify return values or limit what attributes are
    available and then make assertions about how they have been used.

    Tutorials: http://nbviewer.ipython.org/gist/jiffyclub/3701929

"""

import mock  # Python 3.3+ is available as unittest.mock
import json


def assign_attributes_example():
    """ Create a basic Mock() object, assign attributes, view attributes """

    myMock = mock.Mock(greeting="hello")  # Create Mock object with attribute
    print type(myMock)  # <class 'mock.Mock'>
    print myMock.greeting  # 'hello'
    myMock.greeting = "hello world!"  # Change attribute
    print "Changed attribute is now: ", myMock.greeting


def return_value_example():
    """ Use Mock to stand in for a function; return a value no matter what """
    myMock = mock.MagicMock()  # Create Mock or MagicMock(), doesn't matter
    myMock.return_value = 10  # no matter what, returns this value
    print myMock(6, 9, "stuff")  # prints out 10, doesn't matter what input is


def assert_called_with_example():
    """
        Mock objects remember the most recent way they were called using
        the function 'assert_called_with'.  If an assert passes, nothing
        happens.  If an assert fails, an Assertion Error will appear.
    """
    myMock = mock.MagicMock()
    myMock(6, 9, "stuff")

    myMock.assert_called_with(6, 9, "stuff")  # passes if nothing happens

    myMock.assert_called_with(1, 3, "otherstuff")
    # if doesn't match, Assertion Error: Expected Call: mock(1, 3, 'otherstuff')
    # Actual call: mock(6, 9, 'stuff')


def noncallable_mock_example():
    """
        a NonCallableMock is the same as a plain Mock except it can't be
        called.  This is mocking a non-callable class
    """
    my_mock_class = mock.NonCallableMock()
    my_mock_class.some_method.return_value = 42
    print my_mock_class.some_method(6, 9)  # 42

    my_mock_class.some_method.assert_called_once_with(6, 9)  # Passes


def side_effects_example():
    """
        Mock objects can have side effects when called instead of a simple
        return value.  For example, you might want to raise an exception to
        make sure that your test responds correctly.  Use 'side_effect'
    """
    mock_func_w_side_effect = mock.Mock()

    # Create side_effect of raising an error
    mock_func_w_side_effect.side_effect = ValueError('Wrong!')
    mock_func_w_side_effect()  # Raises a ValueError: Wrong!

    # Create side_effect of a function
    mock_func_w_side_effect.side_effect = lambda x, y: y + x
    print mock_func_w_side_effect('spam', 'SPAM')  # SPAMspam


def func_with_json(d):
    """ Serialize an object into a JSON formatted str; our sample function """
    return json.dumps(d)


def patching_example():
    """
        There's a few different ways to use patch as a function, replacing an
        object inside a function or class, or as a class decorator.
    """

    d = {'a': 1, 'b': [2, 3]}  # a simple input for 'func_with_json'

    # use mock.patch to replace a function (json.dumps) in context block
    with mock.patch('json.dumps') as mock_dumps:
        mock_dumps.return_value = 'JSON'  # json.dumps will return this value
        r = func_with_json(d)  #
        assert r == 'JSON'
        mock_dumps.assert_called_once_with(d)

    print json.dumps(d)  # json.dumps now back to normal
    # {"a": 1, "b": [2, 3]}

    # use mock.patch to replace a function (json.dumps) in a test function
    @mock.patch('json.dumps')
    def test_func_with_json(mock_dumps):
        mock_dumps.return_value = 'JSON'
        r = func_with_json({'c': {'d': [4]}})
        assert r == 'JSON'
        mock_dumps.assert_called_once_with(d)  # this should fail
        # AssertionError: Expected call: dumps({"a": 1, "b": [2, 3]})
        # Actual call: dumps({"c": {"d": [4]}})

    test_func_with_json()


class Pet(object):
    """ Just a class to practice mocking with """
    def __init__(self):
        self.name = 'Testing'

    def say_name(self):
        print "My name is ", self.name


if __name__ == '__main__':

    #assign_attributes_example()
    #return_value_example()
    #assert_called_with_example()
    #noncallable_mock_example()
    #side_effects_example()
    patching_example()

