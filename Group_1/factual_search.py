#!/usr/bin/python

import urllib
import json
import sys
from factual import Factual

import inspection

FACTUAL_KEY = "h38jlPEHTOOI1CjxUD2OY6lXc181MrDfXZE6BMJI"
FACTUAL_SECRET = "oOmtPt9dfknPS63W2TYrExQPX49HvsVQOKFhiFZN"

#This is the main method for clients to use
#It returns a string of useful information given the string inputted by the client
#It calls getSearchData and using the result gets the sanitation grade (if it exists) and calls the printVitals method which returns information about the restaurant in string form
def getSearchString(inputs):
    data = getSearchData(inputs)
    if(data != {}):
        rating = inspection.getGradeForZip(data["name"],data["postcode"])
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

 
#This method is called by the getSearchString method
#getSearchString gives getSearchData the string from the client
#This method turns the string into a list, determines which search method to use based on how many parameters the list has, and calls the appropriate search
#The method then returns the raw data (in dictionary form) from the search
def getSearchData(inputs):
    result = {}
    try:
        parameters = inputs.split(',')
    except AttributeError:
        parameters = []
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

#Searching with just the search term
def search(name):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')
    
    result = table.search(name)
    try:
        return result.data()[0]
    except IndexError:
        return {}

#Search limited to a particular zipcode
def searchZip(name, zipcode):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'postcode': zipcode}).limit(1)
    result = filters.search(name)
    try:
        return result.data()[0]
    except IndexError:
        return {}

#Search with an exact address (has not worked in testing)
def searchAddress(name,street,city,state):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'address': street, 'locality':city, 'region': state}).limit(1)
    result = filters.search(name)
    try:
        return result.data()[0]
    except IndexError:
        return {}

#Search with a city and state (has not worked in testing)
def searchCity(name,city,state):
    f = Factual(FACTUAL_KEY, FACTUAL_SECRET)
    table = f.table('restaurants-us')

    filters = table.filters({'locality': city, 'region': state}).limit(1)
    result = filters.search(name)
    try:
        return result.data()[0]
    except IndexError:
        return {}

#Takes the restaurant's entry from factual (a dictionary) and extracts certain fields
#It returns a string of important information
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
