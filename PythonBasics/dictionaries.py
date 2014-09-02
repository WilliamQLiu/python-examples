""" How to use Python's dictionaries """
# dicts are key:value pairs

def dict_example_1():
    """ Example of how to initialize and call a dict one way """
    print "Dict Example 1"
    phonebook = {}
    phonebook["John"] = 938477566
    phonebook["Jack"] = 938377264
    phonebook["Jill"] = 947662781
    print phonebook # {'Jill': 947662781, 'John': 938477566, 'Jack': 938377264}
    print phonebook['Jill'] # prints Jill's number: 947662781

    #Remove a specified index
    del phonebook["John"]
    phonebook.pop("Jack")
    print "After removing John and Jack"
    print phonebook
    print "\n"

def dict_example_2():
    """ Example of how to initialize and call a dict another way """
    print "Dict Example 2"
    phonebook = {
        "John" : 938477566,
        "Jack" : 938377264,
        "Jill" : 947662781
    }
    print phonebook
    print "\n"
    
    """ Example of how to iterate over dicts """
    print "Iterating over a dict"
    for name, number in phonebook.iteritems():
        print "Phone number of %s is %d" % (name, number)


if __name__ == '__main__':
    dict_example_1()
    dict_example_2()