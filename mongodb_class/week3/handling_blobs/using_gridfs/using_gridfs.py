#!/usr/bin/env python

import pymongo
import gridfs

# establish a connection to the database
connection = pymongo.MongoClient()

#get a handle to the test database
db = connection.test
file_meta = db.file_meta
file_used = "sample_128_mb.txt"

def main():

    grid = gridfs.GridFS(db, "text")
    fin = open(file_used, "r")

    _id = grid.put(fin)
    fin.close()
    print "id of file is", _id

    file_meta.insert( { "grid_id": _id, "filename": file_used})

if __name__ == '__main__':
    main()
