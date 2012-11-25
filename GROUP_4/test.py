#!/usr/bin/python

from factual import *
import json
import urllib

FACTUAL_KEY = "ayza4T1yldZH6VlPIQcFPYEtRs3CfhTp43Cs9Ulb"
FACTUAL_SECRET = "qsxNCmjAEt0PUlYO6ZYisIh6lFQbtcCuFi6Nizyt"
UPCOMING_KEY = "74fb5c7bc0"
def upcomingtest():
    request = urllib.urlopen("http://upcoming.yahooapis.com/services/rest/?api_key=74fb5c7bc0&method=event.search&search_text=killers&metro_id=1&format=json")
    result  = json.loads(request.read())
    print result;

def main():
    print "---------------TEST OF FACTUAL API-----------------"
    factual = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    
    table = factual.table('places')
    
    q1 = table.search("sushi Santa Monica")
    print q1.data()[1]
    print q1.get_url()
    
    q2 = table.filters({'category': "Food & Beverage", 'region': "CA"}).limit(1)
    print q2.data()
    print "---------------TEST OF UPCOMING API-----------------"
    upcomingtest()

if __name__ == '__main__':
    main()
