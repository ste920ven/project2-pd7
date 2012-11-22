#!/usr/bin/python

import urllib
import json
import sys

class Rester:
    def __init__(self,url):
        self.url = url

    def call(self,q):
        urlstring = "%s?%s"%(self.url,q)
        print urlstring
        
        request = urllib.urlopen(urlstring)
        #result = request.read();
        result = json.loads(request.read())
        return result


r = Rester("https://www.googleapis.com/books/v1/volumes")
qstring = "q=dragon+tattoo&key=AIzaSyC7RvStliSi1jKeNrOzUJcWTuLyWmrPFao"

result = r.call(qstring) # remember rester converts from json

#print result
#for r in result['items']:
    #for vol in r['volumeInfo']:
        #print vol['title'], vol['authors']
        #print
    #for vol in r['volumeInfo']:
       #print r['volumeInfo']['title']
        #print r['selfLink']
        #print

print result['items'][0]['volumeInfo']['title'], result['items'][0]['volumeInfo']['previewLink']
