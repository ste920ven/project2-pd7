import urllib2
import json
from pymongo import Connection

def connection():
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate('ml7', 'ml7')
    db = connection['z-pd7-LO']
    return db


def newUser(user):
    db = connection()
    team = "NONE"
    username = {'username': user, 'team': team}
    db.username.save(username)


def test(user):
    db = connection()
    print db.username.find_one({"username": user})

def username(username):
    db = connection()
#have to parse through in order to get at actual data
    d = [x for x in db.username.find({'username':username})]
   # print d
    if len(d) == 0:
        print "This username does not exist"
        return -1
    else:
        res = db.username.find_one({"username": username})['username']
        print res


def deleteAll():
    db = connection()
    db.username.remove({});  



newUser("Leopold")
#test("Leopold")
username("Leopold")
username("Raquel")

