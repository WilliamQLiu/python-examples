__author__ = 'aje'


import pymongo
import sys
import time


connection = pymongo.MongoReplicaSetClient("localhost:27017,localhost:27018,localhost:27019",
                                           replicaSet="m101")

db = connection.m101
test = db.test
test.remove()   # clear collection

def writesome():
    # let's do some inserting
    for i in range(0,1000000):
        doc = {'i':i}
        try:
            test.insert(doc)
            print "Inserted " + str(i)

        except:
            print sys.exc_info()[0]


        time.sleep(.5)



writesome()