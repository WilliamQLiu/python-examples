""" How to use Python's Class and Object"""
# Class is CarClass(), which is basically a template
# car1 and car2 are Objects from Class CarClass()

class CarClass():
    """ The template for cars, has own attributes """
    cartype="stuff"
    name = "blah"
    worth = 1000
    def report_back(self):
        print "Car type is: ", self.cartype
        print "Car name is: ", self.name
        print "Car worth is: ", self.worth, "\n"

if __name__ == '__main__':

    # Create first object, then assign attributes
    car1 = CarClass()
    car1.cartype="red convertible"
    car1.name="Fer"
    car1.worth=60000
    car1.report_back()

    # Create second object, then assign attributes
    car2 = CarClass()
    car2.cartype="blue van"
    car2.name="Jump"
    car2.worth=10000
    car2.report_back()
