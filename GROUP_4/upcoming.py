
import json

import urllib
import pprint

UPCOMING_KEY = "74fb5c7bc0"

def sendRequest(requestString):
    request = urllib.urlopen(requestString)
    result  = json.loads(request.read())
    return result;

def getStateId(x):
    request = urllib.urlopen("http://upcoming.yahooapis.com/services/rest/?api_key=74fb5c7bc0&method=metro.getStateList&country_id=1&format=json")
    result = json.loads(request.read())
    states = {"name": "id"}
    for item in result['rsp']['state']:
        states[item['name']] = item['id']         
    return states[x]

def getEvent(artist,zip_code):
    request = "http://upcoming.yahooapis.com/services/rest/?api_key=74fb5c7bc0&method=event.search&search_text=" + artist + "&location=" + str(zip_code) +"&format=json"
    print request
    print sendRequest(request)



getMusicShow("Comedy",11354)
