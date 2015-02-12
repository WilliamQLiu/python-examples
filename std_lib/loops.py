""" How to do loops in Python """


def for_loop_example():
    """ How to use a simple for-loop to go over a list"""
    print "For Loop Example"
    mylist = [2, 3, 4, 5, 9, 10]
    for x in mylist:
        print x
    print "\n"


def in_xrange_example(start_num, end_num=10):
    """ How to use xrange (can pass in up to two arguments) """
    #print start_num (passed) up to end_num (default 10, prints up to 9)
    print "xrange example given", start_num, "and", end_num
    for x in xrange(start_num, end_num):
        print x
    print "\n"

    # Can also loop through a list in reverse
    for index in reversed(xrange(1, 10, 2)):
        print index  # 9 7 5 3 1


def while_loop_example(number):
    """ How to use while loops """
    print "While Loop example from 0 to", number
    count = 0
    while count < number:
        print count
        count += 1
    print "\n"


def break_example():
    """ How to use break to exit code """
    print "Break Example"
    count = 0
    while True:
        print count
        count += 1
        if count > 5:
            break
    print "\n"


def continue_example():
    """ How to use continue to ignore specific cases """
    print "Continue Example"
    for x in xrange(10):
        # Check if x is even
        if (x % 2 == 0):
            continue
        print x


def iteritems_example():
    """ Can loop through dicts (key, values) using iteritems """
    # Loop through a dict using iteritems() method
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for index, values in knights.iteritems():
        print index, values
        # gallahad the pure
        # robin the brave


def enumerate_example():
    """ How to enumerate across a list to get index and value """
    print "Enumerate Example"
    for index, value in enumerate(['tic', 'tac', 'toe']):
        print index, value


def zip_example():
    """ Go through two lists of equal size with zip """
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for qst, ans in zip(questions, answers):
        print "What is your {0}? It is {1}.".format(qst, ans)


def list_comprehension_example():
    """ A list comprehension is a quick way to generate a list and has the
    following format: result = transform, iteration, filter.
     """
    simple_range = [i for i in range(5)]  # no transform or filter, only iteration
    complex_range = [i * i for i in range(5) if i % 2 == 0]  #transform, iteration, filter

    print simple_range  # [0, 1, 2, 3, 4]
    print complex_range   # [0, 4, 16]


def set_example():
    """
        A set is an unordered collection of distinct hashable objects.
        Common uses include intersection, union, difference, remove dupes
    """
    # To get unique list of items, you can use set()
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in set(basket):
        print f  # orange, pear, apple, banana

    # Can also use sets to compare each other
    a = [1, 2, 3, 4, 5]
    b = [9, 8, 7, 6, 5]

    # Get value(s) in both sets
    same_set = set(a).intersection(b)  # set([5]), Pythonic way
    #same_set = set(a) & set(b)  # same as above, but not Pythonic, don't use
    print type(same_set)  # <type 'set'>
    print same_set  # set([5])
    for value in same_set:  # Get values out of a set
        print value  # 5

    different_set = set(a).difference(b)
    for value in different_set:  # Get values out of a set
        print value  # 1, 2, 3, 4

    union_set = set(a).union(b)
    for value in union_set:  # Get values out of a set
        print value  # 1,2,3,4,5,6,7,8,9  # Note only one 5 value returns

    issubset_set = set(a).issubset(b)
    print issubset_set  # False; every element of a is not in set b

    issuperset_set = set(a).issuperset(b)
    print issuperset_set  # False; every element of b is not in set a


if __name__ == '__main__':
    """Goes through examples of all the loop variations"""
    for_loop_example()
    in_xrange_example(4)  # prints 4,5,6,7,8,9
    in_xrange_example(4, 7)  # prints 4,5,6
    while_loop_example(5)  # prints 0,1,2,3,4
    break_example()  # prints 0,1,2,3,4
    continue_example()  # prints 1,3,5,7
    enumerate_example()
    # prints 0 tic
    #        1 tac
    #        2 toe
    zip_example()
    # What is your name?  It is lancelot
    # What is your quest?  It is the holy grail
    # What is your favorite color?  It is blue
    list_comprehension_example()  # how to do list comprehensions
    set_example()  # how to use sets
