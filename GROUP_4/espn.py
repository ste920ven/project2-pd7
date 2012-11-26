import urllib2
import json

key = '49hvkyvay6f9dtx738jxnj3t'
shared_secret = 'FAfHeFfmASXXHmv6zfztXdHu'


def getTeam(teamId):  
    getTeam =  'http://api.espn.com/v1/sports/baseball/mlb/teams/' + str(teamId) + '?rostertype=active&_accept=application%2Fjson&apikey=49hvkyvay6f9dtx738jxnj3t'
    url= urllib2.urlopen(getTeam)
    result = json.loads(url.read())
    return result

def getLocation(team): 
    result = team["sports"][0]["leagues"][0]["teams"][0]["location"]
    print result
    return result

def getName(team):
    result = team["sports"][0]["leagues"][0]["teams"][0]["name"]
    print result 
    return result

def getTeamNews(teamId):
    news = "http://api.espn.com/v1/sports/baseball/mlb/news/?teams=" + str(teamId) + "&insider=yes&_accept=application%2Fjson&apikey=49hvkyvay6f9dtx738jxnj3t"
    url = urllib2.urlopen(news)
    result = json.loads(url.read())
    for x in range(0,10):
        print "Headline:" +  result["headlines"][x]["headline"]
        print "Description:" + result["headlines"][x]["description"]  + "\n"
   # print result["headlines"][0]["links"]["api"]["news"]


sox = getTeam(2)
getLocation(sox)
getName(sox)
getTeamNews(2)




