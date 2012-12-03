import urllib2
import json
from pymongo import connection

def connection():
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate('ml7', 'ml7')
    db = connection['z-pd7-LO']
    return db



key = '49hvkyvay6f9dtx738jxnj3t'
shared_secret = 'FAfHeFfmASXXHmv6zfztXdHu'


def getTeam(teamId):  
    getTeam =  'http://api.espn.com/v1/sports/baseball/mlb/teams/' + str(teamId) + '?rostertype=active&_accept=application%2Fjson&apikey=' + key
    url= urllib2.urlopen(getTeam)
    result = json.loads(url.read())
    return result

def getLocation(team): 
    result = team["sports"][0]["leagues"][0]["teams"][0]["location"]
    print "Location: " + result
    return result

def getName(team):
    result = team["sports"][0]["leagues"][0]["teams"][0]["name"]
    print "Team Name: " + result 
    return result

def getHeadline(teamId, x):
    headlines = ""
    news = "http://api.espn.com/v1/sports/baseball/mlb/news/?teams=" + str(teamId) + "&insider=yes&_accept=application%2Fjson&apikey=49hvkyvay6f9dtx738jxnj3t"
    url = urllib2.urlopen(news)
    result = json.loads(url.read())
   # for x in range(0,10):
   # print "Headline: " +  result["headlines"][x]["headline"]
   # print "Description: " + result["headlines"][x]["description"]  + "\n"
   # print result["headlines"][0]["links"]["api"]["news"]
    headlines +=  result["headlines"][x]["headline"] + "\n" 
    print headlines
    return headlines

def getDescription(teamId, x):
    headlines = ""
    news = "http://api.espn.com/v1/sports/baseball/mlb/news/?teams=" + str(teamId) + "&insider=yes&_accept=application%2Fjson&apikey=49hvkyvay6f9dtx738jxnj3t"
    url = urllib2.urlopen(news)
    result = json.loads(url.read())
   # for x in range(0,10):
   # print "Headline: " +  result["headlines"][x]["headline"]
   # print "Description: " + result["headlines"][x]["description"]  + "\n"
   # print result["headlines"][0]["links"]["api"]["news"]
    headlines += "Description: " + result["headlines"][x]["description"]  + "\n\n"
    print headlines
    return headlines






def getTeamID(t):
    if t == "Baltimore Orioles":
        return 1
    if t == "Boston Red Sox":
        return 2
    if t == "Los Angeles Angels":
        return 3
    if t == "Chicago White Sox":
        return 4
    if t == "Cleveland Indians":
        return 5
    if t == "Detroit Tigers":
        return 6
    if t == "Kansas City Royals":
        return 7
    if t == "Milwaukee Brewers":
        return 8
    if t == "Minnesota Twins":
        return 9
    if t == "New York Yankees":
        return 10 
    if t == "Oakland Athletics":
        return 11
    if t == "Seattle Mariners":
        return 12
    if t == "Texas Rangers":
        return 13
    if t == "Toronto Blue Jays":
        return 14
    if t == "Atlanta Braves":
        return 15
    if t == "Chicago Cubs":
        return 16
    if t == "Cincinnati Reds":
        return 17
    if t == "Houston Astros":
        return 18
    if t == "Los Angeles Dodgers":
        return 19
    if t == " Washington Nationals":
        return 20
    if t == "New York Mets":
        return 21
    if t == "Philadelphia Phillies":
        return 22
    if t == "Pittsburgh Pirates":
        return 23
    if t == "St. Louis Cardinals":
        return 24
    if t == "San Diego Padres":
        return 25
    if t == "San Francisco Giants":
        return 26
    if t == "Colorodo Rockies":
        return 27
    if t == "Miami Marlins":
        return 28
    if t == "Arizona Diamondbacks":
        return 29
    if t == "Tampa Bay Rays":
        return 30
"""

x = getTeamID("Miami Marlins")
sox = getTeam(x)
getLocation(sox)
getName(sox)
getHeadline(x, 0)
getDescription(x, 0)
"""




orioles = 1
sox = 2
angels = 3
whitesox = 4
indians = 5
tigetrs = 6
royals = 7
brewers = 8
twins = 9
yankees = 10
oakland = 11
mariners = 12
rangers = 13
bluejays = 14
braves = 15
cubs = 16
reds = 17
astros = 18
dodgers = 19
nationals = 20
mets = 21
phillies = 22
pirates = 23
cardinals = 24
padres = 25
giants = 26
rockies = 27
marlins = 28
diamondbacks = 29
rays = 30

