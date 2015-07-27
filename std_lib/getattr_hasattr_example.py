"""
    Using getattr and hasattr

    Python's getattr function fetches an attribut from an object;
    it allows you to call methods based on the contents of a string instead
    of typing the method name.  For example:
        value = obj.attribute
        value = getattr(obj, "attribute")
    If attribute exists, value is returned.  If not exists, get AttributeError

    What do you use getattr (and hasattr) for?

    getattr references to a function without knowing its name until run-time

    getattr is also commonly used to map data to functions (i.e. a dispatcher)
    In Django, getattr maps the web request's URL to a function.
    http://www.example.com/customers/list turns into 'customers' and 'list'.
    It then searches for a controller class say 'CustomerController', creates
    an instance of the class and then uses 'getattr' to get its 'list' method.
    This allows you to extend the functionality of a web application: just
    add new methods to the controller classes, then create links in your pages
    that use the appropriate URLs for those methods.

    This is known as a Dispatcher.  For example, if you had a
    program that could output data in a variety of different formats, you
    could define separate functions for each output format and use a single
    dispatch function to call the right one.
"""


import sys
import os


class Employee(object):
    """ Base Class for Employees """
    __secretEmpCount=0  # __ means a hidden attribute not visible to outsiders

    def __init__(self, name, salary):
        print "Initializing Employee"
        self.name = name
        self.salary = salary
        Employee.__secretEmpCount += 1

    def __str__(self):
        return "This is a base class for Employees"

    def __getattr__(self, name):
        """ Gets the attribute name and returns function based on name """
        if name == 'special':
            return 'Hey, I know you'
        elif name == 'secret':
            return 'I know you too!'
        else:
            raise AttributeError, name

    def displayCount(self):
        """ Display count of how many employees total """
        print "Total Employee(s): %d" % Employee.__secretEmpCount

    def displayEmployee(self):
        """ Display details about employee """
        print "Name : ", self.name, ", Salary: ", self.salary


class LogDispatcher(object):
    """
        Example of using getattr as a Dispatcher - i.e. map data to function
    """
    def __init__(self):
        self.os = os.name
    def __getattr__(self, name):
        """ Look for a 'save' attribute or returns attribute specified """
        if name == 'save':
            try:
                # try to dynamically return a save method appropriate for user
                return getattr(self, self.os)
            except:
                # nothing found, return a default save method
                return getattr(self, '_save')
        else:
            return getattr(self, name)

    # each of these methods can have logic specific to each system
    def nt(self):
        print 'Saving on a nt machine'
    def posix(self):
        print 'Saving on a posix machine'
    def osx(self):
        print 'Saving on a osx machine'
    def unix(self):
        print 'Saving on a unix machine'
    def _save(self):
        print 'Saving on an unknown operating system'
    def get_os(self):
        print os.name


def getattr_on_object():
    """
        getattr can be used on any object that supports dotted notation
        (modules, functions, classes); for custom classes, just implement the
        __getattr__ method.
    """

    # Module Example
    print "PATH IS "
    print type(sys)  # <type 'module'>
    path_details = getattr(sys, "path")
    #print sys.path  # Same as above line
    print path_details

    # builtin_function_or_method Example
    print "LEN MEANS "
    print type(len)  # <type 'builtin_function_or_method'>
    doc_details = getattr(len, "__doc__")
    print doc_details

    # Class Example
    print "CLASS EXAMPLE"
    emp1 = Employee(name="Will", salary="50000")
    print emp1  # "This is a base class for Employees"
    print emp1.name  # Will
    emp1.displayCount()  # 1

    # Getting attribute
    try:
        temp = getattr(emp1, 'name')
    except AttributeError:
        print "Cannot find attribute"
    else:
        print "Got attribute of: ", temp

    # Getting custom __getattr__
    print emp1.special  # Hey, I know you
    print emp1.secret  # I know you too!
    #print emp1.another  # AttributeError: another


def hasattr_example():
    """
        hasattr just calls getattr; the arguments are an object and a string.
        Returns True if the string is the name of one of the object attr.
        Returns False if not.
    """
    emp2 = Employee(name="Laura", salary="1000000")
    print hasattr(emp2, 'name')  # True
    print hasattr(emp2, 'special')  # True
    print hasattr(emp2, 'restaurant')  # False
    print hasattr(emp2, '__secretEmpCount')  # False, can't find because __


def dispatcher_example():
    """ Map data to functions; can call it two ways, both the same """
    mylogger = LogDispatcher()

    # Option 1 - save the attribute, then call it
    save_func = mylogger.save
    save_func()  # Saving on a posix machine

    # Option 2 - call it directly
    mylogger.save()  # Saving on a posix machine
    mylogger.get_os()  # posix


if __name__ == '__main__':
    getattr_on_object()
    hasattr_example()
    dispatcher_example()
