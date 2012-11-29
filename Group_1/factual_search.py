#!/usr/bin/python

import urllib
import json
import sys
from factual import Factual

import inspection

FACTUAL_KEY = "h38jlPEHTOOI1CjxUD2OY6lXc181MrDfXZE6BMJI"
FACTUAL_SECRET = "oOmtPt9dfknPS63W2TYrExQPX49HvsVQOKFhiFZN"

  
def searchZip(name, zipcode):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'postcode': zipcode}).limit(1)
    result = filters.search(name)
    #print result.data()[0]
    try:
        return result.data()[0]
    except IndexError:
        return {}

def getSearchData(inputs):
    result = {}
    parameters = inputs.split(',')
    for x in range(0,4):
        parameters.append("")
    for x in range(0,len(parameters)):
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
    if(data != {}):
        rating = inspection.getGradeFor(data["name"])
        print rating
        if(printVitals(data)):
            if(rating):
                r = printVitals(data) + "Sanitation Grade: " + rating
            else:
                r = printVitals(data)
        else:
            r = "returning something"
    else:
        r = "Search returned no results"
        
    print r
    return r

def search(name):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')
    
    result = table.search(name)
    #print result.data()[0]
    try:
        return result.data()[0]
    except IndexError:
        return {}

def searchAddress(name,street,city,state):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'address': street, 'locality':city, 'region': state}).limit(1)
    result = filters.search(name)
    #print result.data()[0]
    try:
        return result.data()[0]
    except IndexError:
        return {}

def searchCity(name,city,state):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'locality': city, 'region': state}).limit(1)
    result = filters.search(name)
    #print result.data()[0]
    try:
        return result.data()[0]
    except IndexError:
        return {}

#In the future printVitals can be edited or replaced to reflect what we actually want to return to the user
def printVitals(data):
    string = ""
    string = string + "Name: " + data["name"] + '\n'
    #string = string + "Category: " + data["category"] + '\n'
    string = string + "Address: " + data["address"] + " " + data["locality"] + ", " + data["region"] + " " + data["postcode"] + '\n'
    try:
        string = string + "Rating: " + str(data["rating"]) + '/5\n'
    except KeyError:
        string = string + "Rating: No rating" + '\n'
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

getSearchString("Bar,New York,NY")
 
