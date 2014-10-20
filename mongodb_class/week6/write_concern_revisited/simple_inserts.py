
import pymongo

read_pref = pymongo.read_preferences.ReadPreference.SECONDARY

c = pymongo.MongoClient(host="mongodb://localhost:27017",
                        replicaSet="rs1",
                        w=3, wtimeout=10000, j=True, 
                        read_preference=read_pref)

db = c.m101
people = db.people

print "inserting"
people.insert({"name":"Andrew Erlichson", "favorite_color":"blue"})
print "inserting"
people.insert({"name":"Richard Krueter", "favorite_color":"red"})
print "inserting"
people.insert({"name":"Dwight Merriman", "favorite_color":"green"})





