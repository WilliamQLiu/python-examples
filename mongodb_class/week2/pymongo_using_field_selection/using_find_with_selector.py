
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
scores = db.scores


def find():

    print "find, reporting for duty"

    query = {'type':'exam'}
    selector = {'student_id':1, '_id':0}

    try:
        iter = scores.find(query, selector)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in iter:
        print doc
        sanity += 1
        if (sanity > 10):
            break
        


def find_one():

    print "find one, reporting for duty"
    query = {'student_id':10}
    
    try:
        doc = scores.find_one(query)
        
    except:
        print "Unexpected error:", sys.exc_info()[0]

    
    print doc


#find_one()
find()
