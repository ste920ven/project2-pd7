import urllib2
import json
from pymongo import Connection
import espn
import movies
import upcoming

def connection():
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate('ml7', 'ml7')
    db = connection['z-pd7-LO']
    return db


def newUser(user):
    db = connection()
    team = "NONE"
    music = "NONE"
    mood = "NONE"
    zipcode = "NONE"
    username = {'username': user, 'team': team, 'music': music, 'mood': mood, 'zip': zipcode}
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
        return 1


def saveTeamID(username, teamName):
    db = connection()
    teamId = espn.getTeamID(teamName)
    db.username.update({"username": username}, {'$set':{ 'team': teamId}})

def saveMusic(username, genre):
    db = connection()
    db.username.update({"username":username}, {'$set':{'music': genre}})

def saveMood(username, mood):
    db = connection()
    db.username.update({"username":username}, {'$set':{'mood': mood}})

def saveZip(username, zipcode):
    db = connection()
    db.username.update({"username":username}, {'$set':{'zip': zipcode}})

def getTeamID(username):
    db = connection()
#have to parse through in order to get at actual data
    d = [x for x in db.username.find({'username':username})]
   # print d
    if len(d) == 0:
        print "This username does not exist"
        return -1
    else:
        res = db.username.find_one({"username": username})['team']
        if res == "NONE":
            return -1
        print res
        return res

def getGenre(username):
    db = connection()
#have to parse through in order to get at actual data
    d = [x for x in db.username.find({'username':username})]
     # print d
    if len(d) == 0:
        print "This username does not exist"
        return -1
    else:
        res = db.username.find_one({"username": username})['music']
        if res == "NONE":
            return -1
        print res
        return res

def getCategory(username):
    db = connection()
#have to parse through in order to get at actual data
    d = [x for x in db.username.find({'username':username})]
     # print d
    if len(d) == 0:
        print "This username does not exist"
        return -1
    else:
        res = db.username.find_one({"username": username})['mood']
        if res == "NONE":
            return -1
        print res
        return res

def getZip(username):
    db = connection()
#have to parse through in order to get at actual data
    d = [x for x in db.username.find({'username':username})]
     # print d
    if len(d) == 0:
        print "This username does not exist"
        return -1
    else:
        res = db.username.find_one({"username": username})['zip']
        if res == "NONE":
            return -1
        print res
        return res

def inUse(username):
    db = connection()
#have to parse through in order to get at actual data
    d = [x for x in db.username.find({'username':username})]
    if len(d) > 0:
        print 1
        return 1
    else:
        return -1



def deleteAll():
    db = connection()
    db.username.remove({});  


deleteAll()


newUser("Leopold")
saveTeamID("Leopold", "New York Mets")
saveZip("Leopold", 10023)
saveMusic("Leopold", "blues")
username("Leopold")
test("Leopold")
getTeamID("Leopold")
getZip("Leopold")
inUse("Leopold")
