#!/usr/bin/python

import urllib
import json
import sys
from factual import Factual

FACTUAL_KEY = "h38jlPEHTOOI1CjxUD2OY6lXc181MrDfXZE6BMJI"
FACTUAL_SECRET = "oOmtPt9dfknPS63W2TYrExQPX49HvsVQOKFhiFZN"

  
def searchZip(name, zipcode):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'postcode': zipcode}).limit(1)
    result = filters.search(name)
    #print result.data()[0]
    return result.data()[0]

def getSearchData(inputs):
    result = {}
    parameters = inputs.split(',')
    for x in parameters:
        parameters[x] = parameters[x].lstrip().rstrip()

    if(parameters[3]):
        result = searchAddress(parameters[0],parameters[1],parameters[2],parameters[3])
    elif(parameters[2]):
        result = searchCity(parameters[0],parameters[1],parameters[3])
    elif(parameters[1]):
        result = searchZip(parameters[0],parameters[1])
    elif(parameters[0]):
        result = search(parameters[0])
    
    return result

def getSearchString(input):
    data = getSearchData(input)
    return printVitals(data)

def search(name):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')
    
    result = table.search(name)
    #print result.data()[0]
    return result.data()[0]

def searchAddress(name,street,city,state):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'address': street, 'locality':city, 'region': state}).limit(1)
    result = filters.search(name)
    #print result.data()[0]
    return result.data()[0]

def searchCity(name,city,state):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'locality': city, 'region': state}).limit(1)
    result = filters.search(name)
    #print result.data()[0]
    return result.data()[0]

#In the future printVitals can be edited or replaced to reflect what we actually want to return to the user
def printVitals(data):
    string = ""
    string = string + "Name: " + data["name"] + '\n'
    string = string + "Category: " + data["category"]
    string = string + "Address: " + data["address"] + " " + data["locality"] + ", " + data["region"] + " " + data["postcode"] + '\n'
    string = string + "Rating: " + str(data["rating"]) + '\n'
    print string
    return string

#The following two methods are leftover from the proof, but could still be useful
def searchAndPrintVitals(name):
    data = search(name)
    string = ""
    string = string + "Name: " + data["name"] + '\n'
    string = string + "Category: " + data["category"]
    string = string + "Address: " + data["address"] + " " + data["locality"] + ", " + data["region"] + " " + data["postcode"] + '\n'
    string = string + "Rating: " + str(data["rating"]) + '\n'
    print string
    return string

def searchAndPrintVitalsWZip(name, zipcode):
    data = searchZip(name, zipcode)
    string = ""
    string = string + "Name: " + data["name"] + '\n'
    string = string + "Category: " + data["category"]
    string = string + "Address: " + data["address"] + " " + data["locality"] + ", " + data["region"] + " " + data["postcode"] + '\n'
    string = string + "Rating: " + str(data["rating"]) + '\n'
    print string
    return string
 
