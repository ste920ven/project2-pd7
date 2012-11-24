import urllib
import json
import sys
import oauth.oauth as oauth
# from python-oauth2/example import client

#Consumer Key: 	        ApZCUk_31sWxt_hn1XTRkQ
#Consumer Secret: 	UT7JbF5E12etMMT8xkWkN7GyDHM
#Token:          	PR_LEKH3XahBYvtWj5YYDLkXpWO2FfKf
#Token Secret:  	HiSN27O4Y35sx8arhOQsfdHz2m4

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

def search():
    r = Rester("http://api.yelp.com/v2/search")
    results = r.call("term=food&location=San+Francisco")
    print results

search()

