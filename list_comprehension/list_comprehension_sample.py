""" Notes on how to do comprehensions in Python with reference to ...
        * list comprehension: PEP 2020 - http://legacy.python.org/dev/peps/pep-0202/
        * dict comprehension: http://legacy.python.org/dev/peps/pep-0274/
        * simple generators: http://legacy.python.org/dev/peps/pep-0255/
        * generator expressions: http://legacy.python.org/dev/peps/pep-0289/
    """

def list_comp_example():
    """ PEP 202 - list comprehensions provide a more concise way to create lists
        in situations where map() and filter() and/or nested loops is used """
    print "Example 1:"
    print [i for i in range(10)]  # [0,1,2,3,4,5,6,7,8,9]

    print "Example 2:"
    print [i for i in range(20) if i%2==0]  #[0,2,4,6,8,10,12,14,16,18]


def invert(d):
    """ Used for dict_comp_example > Example 4; flips dict's keys and values """
    return {v : k for k, v in d.iteritems()}

def dict_comp_example():
    """ PEP 274 - similar to list comprehensions, but returns a dict objects
        instead of list objects """
    print "Example 1:"
    print {i : chr(65+i) for i in range(4)}  # {0:'A', 1:'B', 2:'C', 3:'D'}

    print "Example 2:"
    someDict = {0:'A', 1:'B', 2:'C'}
    print {k : v for k, v in someDict.iteritems()} == someDict.copy()  # True

    print "Example 3:"
    list_of_email_addrs = ['will@fake.com', 'wliu@fake.com']
    print {x.lower() : 1 for x in list_of_email_addrs}
    #{'will@fake.com': 1, 'wliu@fake.com': 1}

    print "Example 4:"
    d = {0:'A', 1:'B', 2:'C', 3:'D'}
    print invert(d)  # {'A':0, 'B':1, 'C':2, 'D':3}

    print "Example 5:"
    print {(k, v): k+v for k in range(4) for v in range(4)}
    # {(0, 1): 1, (1, 2): 3, (3, 2): 5, (0, 0): 0, (3, 3): 6, (3, 0): 3,
    #  (3, 1): 4, (2, 1): 3, (0, 2): 2, (2, 0): 2, (1, 3): 4, (2, 3): 5,
    #  (2, 2): 4, (1, 0): 1, (0, 3): 3, (1, 1): 2}


def simple_generator_example():
    """ PEP 255 - a generator is simply a function that returns an object on
        which you can call next so that for every call it returns some value
        until it raises a StopIteration exception"""
    sum_of_first_n = sum(xrange(1000000))
    print "Example 1:"
    print sum_of_first_n  # 499999500000


def generator_expressions():
    """ PEP 289 - generator expressions are high performance, memory efficient
        generalization of list comprehensions and generators """
    print "Example 1:"
    print sum(x*x for x in range(10))  #285

if __name__ == '__main__':
    list_comp_example()
    dict_comp_example()
    simple_generator_example()
    generator_expressions()
