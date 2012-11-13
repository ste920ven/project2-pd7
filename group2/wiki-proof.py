import urllib2
import json

def getTitle():
    request=urllib2.urlopen("http://en.wikipedia.org/w/api.php?format=json=&action=query&list=random&rnnamespace=0")
    result = json.loads(request.read())
    return request

if __name__ == "__main__":
    getTitle()
