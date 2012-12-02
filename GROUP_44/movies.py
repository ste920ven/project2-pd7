
import json
import urllib
import pprint

RT_KEY = "h3mbh7bszyrm9e98tk27zkbq"

def sendRequest(requestString):
    request = urllib.urlopen(requestString)
    result  = json.loads(request.read())
    return result

def requestUpcoming():
    return  sendRequest("http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?apikey=h3mbh7bszyrm9e98tk27zkbq&page_limit=50")

def findMovie(name):  
        return sendRequest("http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=h3mbh7bszyrm9e98tk27zkbq&q=" + name + "&page_limit=1")

def getMovieNames():
    x = requestUpcoming()
    ids = []
    for item in x['movies']:
    	ids.append(item['title'])		
    
    return ids

def getSynopsis(title):
    x = findMovie(str(title))
    details = {"title":"synopsis"}
    for item in x['movies']:
        return item["synopsis"]

def getPoster(title):
    x = findMovie(str(title))
    for item in x['movies']:
    	return  item['posters']['original']
   
def getReleaseDate(title):
    x = findMovie(str(title))
    for item in x['movies']:
        return  item['release_dates']['theater']

def getRating(title):
    x = findMovie(str(title))
    details = {"title":"synopsis"}
    for item in x['movies']:
        return item["mpaa_rating"]

