
import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)


def remove_review_date():
    print "\n\nremoving all review dates"

    # get a handle to the school database
    db=connection.school
    scores = db.scores
    try:
        scores.update({},{'$unset':{'review_date':1}},multi=True)

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
        

# performs wholesale replacement of document
def using_save():

    # get a handle to the school database
    db=connection.school
    scores = db.scores

    print "updating record using save"

    try:
        # get the doc
        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "before: ", score

        # add a review_date
        score['review_date'] = datetime.datetime.utcnow()

        # update the record with convenience method
        scores.save(score)
        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


# performs wholesale replacment of document
def using_update():

    print "updating record using update"
    # get a handle to the school database
    db=connection.school
    scores = db.scores


    try:
        # get the doc
        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "before: ", score

        # add a review_date
        score['review_date'] = datetime.datetime.utcnow()

        # update the record with update. Note that there an _id but DB is ok with that
        # because it matches what was there.
        scores.update({'student_id':1, 'type':'homework'}, score)

        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


def using_set():

    print "updating record using set"
    # get a handle to the school database
    db=connection.school
    scores = db.scores


    try:
        # get the doc
        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "before: ", score

        # update using set
        scores.update({'student_id':1, 'type':'homework'},
                      {'$set':{'review_date':datetime.datetime.utcnow()}})

        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


remove_review_date()
using_save()
remove_review_date()
using_update()
remove_review_date()
using_set()
