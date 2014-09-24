
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)



def insert():

    # get a handle to the school database
    db=connection.school
    people = db.people

    print "insert, reporting for duty"

    doc = {"name":"Andrew Erlichson", "company":"10gen",
              "interests":['running', 'cycling', 'photography']}

    try:
        people.insert(doc)   # first insert
        del(doc['_id'])
        people.insert(doc)   # second insert

    except:
        print "Unexpected error:", sys.exc_info()[0]



insert()

