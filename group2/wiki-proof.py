import urllib2
import simplejson

def getTitle():
    request=urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&format=json&generator=random&redirects=&grnnamespace=0&grnlimit=1")
    result = simplejson.loads(request.read())
    print result
    return result

def getQuote():
     request=urllib2.urlopen("http://www.iheartquotes.com/api/v1/random?format=json&max_lines=2")
     result = simplejson.loads(request.read())
     print result
     return result

if __name__ == "__main__":
    getTitle()
    print '\n'
    getQuote()
