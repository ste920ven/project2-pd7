#!/usr/bin/python

#based on Mr. Z's NYT rest code

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


r = Rester("http://api.nytimes.com/svc/books/v2/lists/hardcover-fiction.json")
qstring = "api-key=4ae78fbc6b2ea9683502ff8e27bafcd5:16:66926374"

result = r.call(qstring) # remember rester converts from json

for r in result['results']:
    for book in r['book_details']:
        print book['title']
        print
