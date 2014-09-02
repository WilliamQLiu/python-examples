""" How to do loops in Python """

def for_loop():
    """ How to use a simple for-loop to go over a list"""
    print "For Loop Example"
    mylist = [2,3,4,5,9,10]
    for x in mylist:
        print x
    print "\n"

def in_xrange(start_num, end_num=10):
    """ How to use xrange (can pass in up to two arguments) """
    #print start_num (passed) up to end_num (with default 10, so prints up to 9)
    print "xrange example given", start_num, "and", end_num
    for x in xrange(start_num, end_num):
        print x
    print "\n"

def while_loop(number):
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
        if (x%2==0):
            continue
        print x

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


if __name__ == '__main__':
    """Goes through examples of all the loop variations"""
    for_loop()
    in_xrange(4) # prints 4,5,6,7,8,9
    in_xrange(4, 7) # prints 4,5,6
    while_loop(5) # prints 0,1,2,3,4
    break_example() # prints 0,1,2,3,4
    continue_example() # prints 1,3,5,7
    enumerate_example() # prints 0 tic
                        #        1 tac
                        #        2 toe
    zip_example() # What is your name?  It is lancelot
                  # What is your quest?  It is the holy grail
                  # What is your favorite color?  It is blue

    # Loop through a list in reverse
    for index in reversed(xrange(1, 10, 2)):
        print index # 9 7 5 3 1

    # To get unique list of items, you can use set()
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in set(basket):
        print f # orange, pear, apple, banana

    # Loop through a dict using iteritems() method
    knights = {'gallahad': 'the pure', 'robin':'the brave'}
    for index, values in knights.iteritems():
        print index, values # gallahad the pure
                            # robin the brave
