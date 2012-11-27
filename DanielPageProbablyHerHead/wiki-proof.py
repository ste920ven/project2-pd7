import urllib2
import simplejson

def getTitle():
    request=urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&format=json&generator=random&redirects=&grnnamespace=0&grnlimit=1")
    result = simplejson.loads(request.read())
    title = (str)(result).find('title',0)
    title = (str)(result)[title+9:((str)(result).find("'", title + 9))]
    print title

def getQuote():
     request=urllib2.urlopen("http://www.iheartquotes.com/api/v1/random?format=json&max_lines=2")
     result = simplejson.loads(request.read())
     quote = (str)(result).find('quote',0)
     quote = (str)(result)[quote+9:((str)(result).find("'", quote + 9))]
     print quote


if __name__ == "__main__":
    getTitle()
    print '\n'
    getQuote()
