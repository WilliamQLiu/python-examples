"""
    How to use the property attribute for classes derived from 'object'

    property() is a built-in function that creates and returns a property
    object with the following:
        property(fget=None, fset=None, fdel=None, doc=None)

    The property object has three methods:
        getter(), which is fget
        setter(), which is fset
        delete(), which is fdel

    Details on Python site:
    class property([fget[, fset[, fdel[, doc]]]])
        fget will get an attribute value; e.g.  myobject.x
        fset will set an attribute value; e.g. myobject.x = value
        fdel will delete an attribute value; e.g. del myobject.x
        doc is the docstring for the property attribute, if not given
          then it is the fget's docstring (if it exists)

    From tutorial: http://www.programiz.com/python-programming/property
"""


class Celsius_P_ND(object):
    """ Creating a Class using the property function, no decorator """

    def __init__(self, temperature=0):
        print "Creating a new object"
        self.set_temperature(temperature)

    def get_temperature(self):
        """ Get temperature """
        print "Getting value"
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temp below -273 is not possible")
        print "Setting value"
        self._temperature = value

    def celsius_to_fahrenheit(self):
        print "Celsius to Fahrenheit is: "
        return (self.get_temperature() * 1.8) + 32

    temperature = property(get_temperature, set_temperature)
    # Above line of code is the same as
    #temperature = property()
    #temperature = temperature.getter(get_temperature)
    #temperature = temperature.setter(set_temperature)


class Celsius_P_D(object):
    """ Creating a Class using the property function as a decorator """
    def __init__(self, temperature=0):
        print "Creating a new object"
        self._temperature = temperature

    def celsius_to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print "Getting value"
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temp below -273 is not possible")
        print "Setting value"
        self._temperature = value


if __name__ == '__main__':

    ### Class with property function, no decorator
    print Celsius_P_ND.__doc__
    A = Celsius_P_ND(37)  # initialize
    print A.temperature  # Get temperature, 37
    print "\n"
    A.set_temperature(40)  # Set temperature using function, 40
    print A.temperature  # Get temperature, 40; notice how it uses get_temperature
    print "\n"
    #print A.set_temperature(-300)  #ValueError
    print A.celsius_to_fahrenheit()  # Do conversion, 104.0; uses get_temperature again
    # Summary: we made the getter as function 'get_temperature' and the
    # setter as function 'set_temperature'

    ### Class with property function as a decorator
    print Celsius_P_D.__doc__
    B = Celsius_P_D(37)  # initialize
    print B.temperature  # Get temperature, 37
    print B.celsius_to_fahrenheit()  # Get temperature, 98.6
    B.temperature = -30  # Setting value
    print B.temperature
    # Summary: We do not need to define the get_temperature and
    # set_temperature functions, we can just reuse the name temperature while
    # defining our getter and setter functions
