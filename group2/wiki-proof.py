import urllib2
import json

def getTitle():
    request=urllib2.urlopen("http://en.wikipedia.org/w/api.php?format=json=&action=query&list=random&rnnamespace=0")
    result = json.loads(request.read())
    return result

def getQuote():
     request=urllib2.urlopen("http://www.iheartquotes.com/api/v1/random?format=json&max_lines=2")
     result = json.loads(request.read())
     return result


