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

if __name__ == '__main__':
    """Goes through examples of all the loop variations"""
    for_loop()
    in_xrange(4) # prints 4,5,6,7,8,9
    in_xrange(4, 7) # prints 4,5,6
    while_loop(5) # prints 0,1,2,3,4
    break_example() # prints 0,1,2,3,4
    continue_example() # prints 1,3,5,7

