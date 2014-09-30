
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
#db=connection.school
db=connection.students
#scores = db.scores
scores = db.grades


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

    query = {'type':'homework'}

    # Find total items
    num_items_cursor = scores.find().count()
    print "Total number of items is: ", num_items_cursor

    try:

        #cursor = scores.find().skip(4)
        cursor = scores.find(query)
        #cursor = cursor.limit(10)
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    # Students and scores are now in ascending order

    student_id_list = []
    for doc in cursor:  # Go through every item that matched original query
        num = doc['student_id']  # Check the student's id if in list already
        if num not in student_id_list:  # If not in list, then...
            student_id_list.append(num)  # Add user's number to the list
            #print doc
            scores.remove(doc)  # Remove the lowest score from the list
        else:
            pass


    print student_id_list



#find_one()
#find()
find_lowest_delete()
