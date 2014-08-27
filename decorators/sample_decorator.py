""" How to use a simple decorator """

def currency(f):
    """ Takes a function and returns a new function
        Takes a value, puts $ and makes it a string"""
    def wrapper(*args, **kwargs):
        return '$' + str(f(*args, **kwargs))
    return wrapper

#class blah_blah():

#    @currency  # wraps a $ in front of the price
#    def price_with_tax(self, tax_rate_percentage):
#        return price * (1 +(tax_rate_percentage * 0.1))
