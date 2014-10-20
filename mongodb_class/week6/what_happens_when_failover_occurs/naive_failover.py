__author__ = 'aje'


import pymongo
import sys
import time


connection = pymongo.MongoReplicaSetClient("localhost:27017,localhost:27018,localhost:27019",
                                           replicaSet="m101")

db = connection.m101
test = db.test
#test.remove()   # clear collection

def readsome():
    # let's do some inserting
    for i in range(0,1000000):

        item = test.find_one()
        print str(item['i'])

        time.sleep(.5)

def writesome():
    # let's do some inserting
    for i in range(0,1000000):
        doc = {'i':i}

        test.insert(doc)
        print "Inserted " + str(i)

        time.sleep(.5)



readsome()