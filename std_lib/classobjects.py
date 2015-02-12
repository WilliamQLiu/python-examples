"""
    How to use Python's Class

    First example is about creating a class,then creating instances from class
    Class is CarClass(), which is basically a template
    car1 and car2 are Objects from Class CarClass()

    Note that a class doesn't necessarily need 'self', can be any variable
    * _singleleadingunderscore means a weak 'internal use' indicator (when
        class is imported, the objects that start with an _ are not imported)
    * singletrailingunderscore_ means to avoid a conflict with Python keyword
        (e.g. class is now class_)
    * __doubleleadingunderscore means naming a class attribute
    * __doubleleadandtrailunderscore__ means 'magic' objects or attributes;
        don't create these, just use as documented (e.g, __init__, __doc__)

    Docs: https://docs.python.org/2/tutorial/classes.html

    When a new class is created, it uses a few 'magic' methods.
    * __new__(cls, [...]) takes the class and any args to pass to __new__
    * __init__(self, [...]) is the initializer for class/forms the object
    * __del__(self) is the destructor for the object (still remember to
        do things like close a connection or file)




    To Do, learn about:
        inheritance
        class attributes
        __dict__
        subclassing built in types
        __new__
        __getattr__ and __setattr__
        private attributes (single and double underscore)
        classmethods and staticmethods

"""

from os.path import join
import csv


class CarClass():
    """ The template for cars, has own attributes """
    cartype = "stuff"
    name = "blah"
    worth = 1000

    def report_back(self):
        print "Car type is: ", self.cartype
        print "Car name is: ", self.name
        print "Car worth is: ", self.worth, "\n"


class Greeting(object):
    """ Example to see what __init__ and methods do """
    def __init__(self):
        self.message = "Hello"

    def my_method(self, name):
        # When a method is called from a Class,
        # __init__ is the first argment passed (self)
        print self.message + " " + name


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


class FileObject:
    """ Wrapper for file objects to make sure file gets closed on deletion"""
    def __init__(self, filepath='/Users/williamliu/GitHub/python-examples/std_lib', filename='list_chats.csv'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')
        self.lines = 0

    def print_lines(self):
        #print type(self.file)  #<type 'file'>
        try:
            for line in self.file:
                self.lines += 1
                print line
        except:
            print "Error"
        self.file.close()  # close file
        print "Total lines is: ", self.lines

    def __del__(self):
        self.file.close()
        del self.file


if __name__ == '__main__':

    # Create first object, then assign attributes
    car1 = CarClass()
    car1.cartype = "red convertible"
    car1.name = "Fer"
    car1.worth = 60000
    car1.report_back()

    # Create second object, then assign attributes
    car2 = CarClass()
    car2.cartype = "blue van"
    car2.name = "Jump"
    car2.worth = 10000
    car2.report_back()

    # Greeting example
    a = Greeting()  # We do not pass any argument to the __init__ method
    a.my_method("William!")  # Only pass a single argument # 'Hello William!'
    # In our 'my_method', there's actually two arguments passed;
    # 1st arg is always 'self' (from __init__) and 2nd arg is 'William'

    happy_bday = Song(["Happy birthday to you,",
                       "I don't want to get sued",
                       "So I'll stop right there"])
    bulls_on_parade = Song(["They rally around tha family",
                            "With pockets full of shells"])
    happy_bday.sing_me_a_song()
    #Happy birthday to you,
    #I don't want to get sued
    #So I'll stop right there
    bulls_on_parade.sing_me_a_song()
    #They rally around tha family
    #With pockets full of shells

    myfile = FileObject()
    print myfile.file  # <open file '/Users/williamliu/GitHub/python-examples/std_lib/list_chats.csv', mode 'r+' at 0x10eac7810>
    myfile.print_lines()  # 22447378,22547145,22273506,...
