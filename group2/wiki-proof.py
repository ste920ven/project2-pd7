import urllib2
import json

def getTitle():
    request=urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&list=random&format=json&rnnamespace=0&rnlimit=1")
    result = json.loads(request.read())
    return result

def getQuote():
     request=urllib2.urlopen("http://www.iheartquotes.com/api/v1/random?format=json&max_lines=2")
     result = json.loads(request.read())
     return result

print "Random Article Title:"
print getTitle()
print "Random Quote:"
print getQuote()
