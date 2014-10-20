
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
#db=connection.school
db=connection.school
#scores = db.scores
students = db.students


def find():

    print "find, reporting for duty"

    query = {'type':'exam'}

    try:
        cursor = scores.find(query).limit(10).skip(30)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in cursor:
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


def find_lowest_delete():

    print "Finding the lowest score per student and deleting record"

    #query = {'type':'homework'}

    num_items_cursor = students.find().count()
    print "Total number of items is: ", num_items_cursor

    #db.students.find( {'scores.0.score': 1.463179736705023 } )
    #db.students.update( {"_id": 0}, {  '$pull': { 'score': 'scores.0.score.2'}} )  # At least this writes

    #db.students.update( {"_id": 0}, {  '$unset': { 'scores.2': 1 } } )  # Working
    #db.students.update( {"_id": 0}, {  '$pull': { 'scores': null } } )

    #db.students.update( {"_id": 0}, {  '$pull': { 'scores': { 'score': 'scores.0.score.2'}} } )

    try:

        #cursor = students.find().skip(4)
        #cursor = students.find(query)
        cursor = students.find()
        #cursor = cursor.limit(1)
        #cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]


    #student_id_list = []
    for doc in cursor:
        justscores = doc['scores']
        print "Justscores: ", justscores
        #for index in justscores:

        first_hw = justscores[2]['score']
        #first_hw = doc['scores'][2]['score']
        print "First HW is: ", first_hw

        second_hw = justscores[3]['score']
        print "Second HW is: ", second_hw

        print "Doc id is:", doc['_id']

        if first_hw < second_hw:
            #students.remove(first_hw)
            #students.remove(justscores[2])
            #try:
                #students.update({"_id":doc['_id']}, { "scores":{ '$pull':{"score":justscores[2]['score']}}} )

            print "Doc is: ", doc['_id']
            students.update( {"_id": doc['_id']}, {  '$unset': { 'scores.2': 1 } } )
            #students.update( {"_id": doc['_id']}, {  '$pull': { 'scores': null } } )

                #print "First HW is:", justscores[2]['score']
            #except:
            #    print "That didn't work"
            #print justscores[2]
            print "First HW removed"
        else:
            #try:
            #students.update({"_id":doc['_id']}, { "scores":{ '$pull':{"score":justscores[3]['score']}}} )
            print "Doc is: ", doc['_id']
            students.update( {"_id": doc['_id']}, {  '$unset': { 'scores.3': 1 } } )
            #students.update( {"_id": doc['_id']}, {  '$pull': { 'scores': null } } )
            #print "Second HW is:", justscores[3]['score']
            #except:
            #    print "That didn't work"
            #students.remove(justscores[3])
            #print justscores[3]
            #students.remove(second_hw)
            print "Second HW removed"

        #students.save(doc)



#find_one()
#find()
find_lowest_delete()
#newquery = students.find( { '_id' : 100 } )#.pretty( )
#print newquery
