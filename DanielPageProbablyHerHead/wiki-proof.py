import urllib2
import simplejson

def getTitle():
<<<<<<< HEAD:group2/wiki-proof.py
    request=urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&format=json&generator=random&redirects=&grnnamespace=0&grnlimit=1")
    result = simplejson.loads(request.read())
    print result
=======
    request=urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&list=random&format=json&rnnamespace=0&rnlimit=1")
    result = json.loads(request.read())
>>>>>>> 84f83ff7b935be7f2d5d989abda44586d641d751:DanielPageProbablyHerHead/wiki-proof.py
    return result

def getQuote():
     request=urllib2.urlopen("http://www.iheartquotes.com/api/v1/random?format=json&max_lines=2")
     result = simplejson.loads(request.read())
     print result
     return result

<<<<<<< HEAD:group2/wiki-proof.py
if __name__ == "__main__":
    getTitle()
    print '\n'
    getQuote()
=======
print "Random Article Title:"
print getTitle()
print "Random Quote:"
print getQuote()
>>>>>>> 84f83ff7b935be7f2d5d989abda44586d641d751:DanielPageProbablyHerHead/wiki-proof.py
