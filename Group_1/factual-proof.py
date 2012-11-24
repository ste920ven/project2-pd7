#!/usr/bin/python

import urllib
import json
import sys
from factual import Factual

FACTUAL_KEY = "h38jlPEHTOOI1CjxUD2OY6lXc181MrDfXZE6BMJI"
FACTUAL_SECRET = "oOmtPt9dfknPS63W2TYrExQPX49HvsVQOKFhiFZN"
#class Rester:
 #   def __init__(self,url):
  #      self.url = url
#
 #   def call(self,q):
  #      urlstring = "%s?%s"(self.url,q)
   #     print urlstring
        
    #    request = urllib.urlopen(urlstring)
     #   #result = request.read();
      #  result = json.loads(request.read())
       # return result

#r = Rester("http://api.v3.factual.com/t/restaurants-us")
#query = ("peets+coffee")



def main():
    #print "---------------TEST OF FACTUAL API-----------------"
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    
    table = f.table('restaurants-us')
    
    q1 = table.search("Ichiro")
    print q1.data()[1]['name']
    #print q1.get_url()
    
    q2 = table.filters({'region': "NY"}).limit(1)
    #print q2.data()
    #print "---------------TEST OF UPCOMING API-----------------"
  
def searchZip(name, zipcode):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'postcode': zipcode}).limit(1)
    result = filters.search(name)
    #print result.data()[0]
    return result.data()[0]

def search(name):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')
    
    result = table.search(name)
    #print result.data()[0]
    return result.data()[0]

def printVitals(name):
    data = search(name)
    string = ""
    string = string + "Name: " + data["name"] + '\n'
    string = string + "Category: " + data["category"]
    string = string + "Address: " + data["address"] + " " + data["locality"] + ", " + data["region"] + " " + data["postcode"] + '\n'
    string = string + "Rating: " + str(data["rating"]) + '\n'
    print string
    return string

def printVitalsWZip(name, zipcode):
    data = searchZip(name, zipcode)
    string = ""
    string = string + "Name: " + data["name"] + '\n'
    string = string + "Category: " + data["category"]
    string = string + "Address: " + data["address"] + " " + data["locality"] + ", " + data["region"] + " " + data["postcode"] + '\n'
    string = string + "Rating: " + str(data["rating"]) + '\n'
    print string
    return string

if __name__ == '__main__':
   # main()
   # search("Sushi")
   # print search("Big Daddy's")["name"]
    printVitals("Restaurant")
    printVitalsWZip("Restaurant", "10128")
    
