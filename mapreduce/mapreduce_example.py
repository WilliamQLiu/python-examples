'''
    Functional programming with Map-reduce examples
    Tutorial: http://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming
    
'''


import random


# Non functional example
a = 0
def increment1():
    global a
    a += 1


# Functional example
def increment2(a):
    return a + 1


# Mapping examples
def what_is_map():
    ''' Don't iterate over lists, do map-reduce.  Here's a few map examples, named and anonymous '''
    name_lengths = map(len, ["Mary", "Isla", "Sam"])
    print name_lengths  # => [4, 4, 3]
    
    # Anonymous functions
    squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
    print squares  # => [0, 1, 4, 9, 16]

    my_inc = map(lambda a: a+1, [1,2,3,4])
    print my_inc  # => [2,3,4,5]


def iteration_example_names():
    '''
        Unfunctional code takes a list of names and returns a random list.
    '''
    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print names  # => ['Mr. Orange', 'Mr. Blonde', 'Mr. Blonde']


def map_example_names():
    '''
        Functional code takes a list of names and returns a random list
    '''
    names = ['Mary', 'Isla', 'Sam']

    secret_names = map(lambda x: random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']), names)
    print secret_names  # => ['Mr. Orange', 'Mr. Pink', 'Mr. Pink']


def what_is_reduce():
    '''
        Reduce takes a function and a collection of items and returns a value by combining (reducing) them like a sum
    '''
    sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
    print sum  # => 10


def iteration_example_count():
    ''' 
        Iterating through a list to create a count
    '''
    sentences = ['Mary read a story to Sam and Isla.', 'Isla cuddled Sam.', 'Sam chortled.']

    sam_count = 0
    for sentence in sentences:
        sam_count += sentence.count('Sam')

    print sam_count  # => 3


def reduce_example_count():
    '''
        Using a reducer to create a sum
    '''
    
    sentences = ['Mary read a story to Sam and Isla.', 'Isla cuddled Sam.', 'Sam chortled.']

    sam_count = reduce(lambda a, x: a +x.count('Sam'),
                   sentences,
                   0)
    print sam_count  # => 3


if __name__ == '__main__':
	  print increment1()  # non-functional
	  print increment2(10)  # functional
	  
	  what_is_map()
	  iteration_example_names()  # non-functional
	  map_example_names()  # functional
	  
	  what_is_reduce()
	  iteration_example_count()  # non-functional
	  reduce_example_count()  # functional

