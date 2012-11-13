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


r = Rester("http://api.v3/factual.com/t/restaurants-us/read")
qstring = "q=Sushi,New York&KEY=drr6uQjOApDhEhzIbCVd63B70xUm71fIIr04CIxN"

result = r.call(qstring) # remember rester converts from json

for rest in result['response']['data']:
    print rest['name']
    print
