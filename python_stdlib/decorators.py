"""
    Decorators take a function object as an argument and returns a function
    object (basically works as a wrapper).  That's why we're reviewing how
    functions work below.

    Functions are first-class citizens, which means they can:
    * assign functions to variables
    * define functions inside other functions
    * functions can be passed as parameters to other functions
    * functions can return other functions
    * inner functions have access to the enclosing scope (i.e. closure)

    So basically decorators (@) are used to make simple modifications to
    callable objects (functions, objects, classes).

    The most common decorators are:
        @property
        @classmethod
        @staticmethod

"""


import functools  # `wraps` is a decorator for updating attributes of the wrapper function


### BEGIN FUNCTIONS

### Example: Assign functions to variables
def greet(name):
    return "Hello " + name


### Example: Define functions inside other functions
def wave(name):
    def acknowledge():
        return "Hey there "

    result = acknowledge() + name
    return result


### Example: Functions can be passed as parameters to other functions
def call_func(func):
    other_name = "Billy"
    return func(other_name)


### Example: Functions can return other functions
def compose_greet_func():
    def acknowledge():
        return "Hello there "

    return acknowledge


### Example: Inner functions have access to the enclosing space (i.e. closure)
def closure_func(name):
    def acknowledge():
        return "Hello there " + name  # this function has access to 'name'

    return acknowledge


### BEGIN DECORATORS

### Function decorators are simply wrappers to existing functions
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


def p_decorate(func):
    """ Wraps string around with <p> tags """
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


### More decorators
def strong_decorate(func):
    """ Wraps string around with <strong> tags """
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    """ Wraps string around with <div> tags """
    def func_wrapper(name):
        return "<div>{0}</div".format(func(name))
    return func_wrapper


### Same as `get_text_clean = p_decorate(get_text_clean)` or if all three decorators then
# `get_text_clean = div_decorate(p_decorate(strong_decorate(get_text_clean)))`
#@div_decorate
#@strong_decorate
@p_decorate
def get_text_clean(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

### Example: Decorating Methods
class Person(object):
    def __init__(self):
        self.name = "Willy"
        self.family = "Liu"

    @p_decorate  # replace with p_decorate_better (just add *args, **kwargs)
    def get_fullname(self):
        return self.name + " " + self.family


### Example: Better Decorator using *args and **kwargs
def p_decorate_better(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))


### Example: Better Decorator (passing arguments to decorators)
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags('p')  # Passes in the 'p' argument
def get_text_best(name):
    return "Hello " + name


### Example: Debugging decorators with functools.wraps
# `wraps` is a decorator for updating attributes of the wrapping
# function (func_wrapper) to those of the original function (get_text_debug)
def tags_debug(tag_name):
    def tags_decorator(func):
        @functools.wraps(func)  # just decorate the function you want to debug with wraps
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags_debug('p')
def get_text_debug(name):
    """ returns some text """
    return "Hello " + name


if __name__ == '__main__':

    ### BEGIN FUNCTIONS

    ### Assign functions to variables
    my_greeting = greet
    print my_greeting("Will")  # Hello Will

    ### Define functions inside other functions
    print wave("Laura")  # Hey there Laura

    ### Functions can be passed as parameters to other functions
    print call_func(greet)  # Hello Billy

    ### Functions can return other functions (functions generating functions)
    my_greeting = compose_greet_func()
    print my_greeting()  # Hello there

    ### Inner functions have access to the enclosing scope (i.e. closure)
    my_greeting = closure_func("John")
    print my_greeting()  # Hello there John

    ### BEGIN DECORATORS

    ### Function decorators are simply wrappers to existing functions
    my_get_text = p_decorate(get_text)
    print my_get_text("Bob")  # <p>lorem ipsum, Bob dolor sit amet</p>

    ### Function taking another func as an argument to generate a new func
    get_text = p_decorate(get_text)
    print get_text("Billy")  # <p>lorem ipsum, Billy dolor sit amet</p>

    ### instead of `get_text = p_decorate(get_text)`, we use the @ decorator
    print get_text_clean("Jean")  # @ to mention name of decorating function

    ### Decorating Methods - methods are functions that expect their first
    # parameter to be a reference to the current object (i.e. use `self`)
    my_person = Person()
    print my_person.get_fullname()  # <p>Willy Liu</p>

    ### Passing arguments to decorators
    print get_text_best("Mike")  # <p>Hello Mike</p>

    ### BEGIN DEBUGGING - how to debug a decorated function
    print get_text_debug.__name__  # get_text_debug
    print get_text_debug.__doc__  # returns some text
    print get_text_debug.__module__  # __main__