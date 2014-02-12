""" How to use Multiple Function Arguments in Python """
# Arguments are *args and **kwargs (i.e. keywords)

def multiple_args(first, second, third, *therest):
    """declare functions which receive a variable number of arguments"""
    print "Multiple Args"
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And the rest %s" % list(therest)

def cheeseshop(kind, *arguments, **keywords):
    print "Do you have any", kind, "?"
    print "I'm sorry, we're all out of", kind
    for x in arguments:
        print x # print through all arguments
    print "-" * 40 
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw] # print through all keyword arguments

if __name__ == '__main__':
    multiple_args('Will', 'Bill', 'Mike', 'Roger', 'Laura')
    cheeseshop("Limburger", "It's very runny, sir",
        "It's really very very runny, sir",
        shopkeeper="William Liu",
        client="Laura Summers",
        sketch="Cheese Shop Sketch")