""" How to use Multiple Function Arguments in Python """
# Arguments are *args and **kwargs (i.e. keywords)

def args_example(*myargs):
    """ How to use an arbitrary number of args with *args (returns list)"""
    print "Args Example"
    for a in myargs:
        print a
    print "\n"

def keyword_args_example(**mykwargs):
    """ How to use an arbitrary number of args with kwargs (returns dict)"""
    print "Keywords Example"
    for a in mykwargs:
        print a, mykwargs[a]
    print "\n"

def multiple_args(first, second, third, *therest):
    """declare functions which receive a variable number of arguments"""
    print "Multiple Args Example"
    print "Multiple Args"
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And the rest %s" % list(therest)
    print "\n"

def cheeseshop(kind, *arguments, **keywords):
    """ Example of using *args (for list) and **kwargs (for dicts) """
    print "CheeseShop Example"
    print "Do you have any", kind, "?"
    print "I'm sorry, we're all out of", kind
    for x in arguments:
        print x # print all arguments: "It's very runny...", "It's really.."
    print "-" * 40 
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw] # print through all keyword arguments

def parrot(voltage, state='a stiff', action='voom'):
    """Unpacking a *kwargs example"""
    print "This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "He's now", state, "!"

def use_lambda(n):
    """ lambdas are funcs that reference variables from the containing scope"""
    return lambda x: x + n

if __name__ == '__main__':
    #How to use *args
    args_example(3)

    #How to use *kwargs
    keyword_args_example(him='will', her='laura', it='sharky')

    # How to use args and *args
    multiple_args('Will', 'Bill', 'Mike', 'Roger', 'Laura')
    
    # How to use *args and *kwargs
    cheeseshop("Limburger", # initial argument
        "It's very runny, sir", #*arguments are a list
        "It's really very very runny, sir",
        shopkeeper="William Liu", #**keywords are dicts (key:value pairs)
        client="Laura Summers",
        sketch="Cheese Shop Sketch")
    
    # How to unpack a list with *args
    args = [3,6]
    print range(*args) # [3,4,5]

    # How to unpack a dict with **kwargs
    mydict = {"voltage":"lots and lots", "state":"DEAD", "action":"talk"}
    parrot(**mydict) # This parrot wouldn't talk if you put lots and ...

    # Using a lambda
    f = use_lambda(10)
    print "Setting value to 10 with a lambda function", f(0)
    print "Setting value +5 with a lambda function", f(5)