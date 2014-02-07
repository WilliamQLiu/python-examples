### Requires pip install fake-factory

from faker import Factory

if __name__ == '__main__':

    faker = Factory.create()

    print faker.name()  # Name 
    print faker.address()  # Address
    print faker.text() # Lots of random text

    print faker.name() # Regenerates a new name