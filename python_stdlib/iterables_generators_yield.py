""" An example of what iterables, generators, and yield does in Python """


def iterables_example():
    """ Iteration is reading items one by one; mylist is an iterable and they
        have the common format 'for ... in'
        Advantage: You can read in as much as you want
        Disadvantage: You store all the values in memory
        What it really means is an iterable is an object that has the
        `__iter__()` method.  That object calls the `next()` method until
        we reach a `StopIteration` exception
    """
    mylist = [1, 2, 3, 4, 5, 6, 7]  # list
    mylistcomp = [x*x for x in range(3)]  # list comprehension

    for index in mylist:
        print index,  # 1, 2, 3, 4, 5, 6, 7

    print "\n"

    for index in mylistcomp:
        print mylistcomp,  #[0, 1, 4] [0, 1, 4] [0, 1, 4]


def generators_example():
    """ Generators are iterators, but you can only iterate over them once
        because they do not store all the values in memory (it's on the fly!)
        Advantage: Doesn't use up all your memory
        Disadvantage: Only iterates once
        This is usually used with `yield` where it runs the function just
        enough to get the next value out of it with yield, then puts it back
        into a suspended state (until the next yield statement)
    """

    mygenerator = (x*x for x in range(3))  # like iterable but () instead of []
    #print type(mygenerator) #<type 'generator'>
    #print mygenerator # <generator object <genexpr> at 0x104843050>
    #print dir(mygenerator)  # generator just calls its own 'next()' method

    for index in mygenerator:
        print index,  #0, 1, 4

    print "\nIndex after is: ", index # 4

    for index in mygenerator:
        print index,  # Doesn't reach here because generators only work once


def yield_example():
    """ yield is used like 'return', except the function returns a
        generator instead of a value.

        To see what a function with 'yield' statements does, do:
        1.) Insert a line: `result = []` at the start of function
        2.) Replace each `yield` expr with `result.append(expr)`
        3.) Insert a line `return result` at the bottom of the function
        4.) That will tell you what the `yield` statement did
        5.) Compare function to original definition
        """
    yield 10
    yield 20
    yield 30


if __name__ == '__main__':

    iterables_example()
    generators_example()
    print yield_example()  # <generator object yield_example at 0x100b2a050>

    for item in yield_example():
        print item, # 10, 20, 30
