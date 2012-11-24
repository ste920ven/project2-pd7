import json
import urllib
from bs4 import BeautifulSoup

#place/nearbysearch location=-33.8670522,151.1957362&radius=500

def getAddress(address):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(address)
    maps_request = urllib.urlopen(geocode_url)
    geo_results = json.loads(maps_request.read())
    print ("\n")
    print geo_results['results'][0]['formatted_address']

def getLatLong(address):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(address)
    maps_request = urllib.urlopen(geocode_url)
    geo_results = json.loads(maps_request.read())
    print ("\n latitude: ")
    print geo_results['results'][0]['geometry']['location']['lat']
    print ("\n longtitude: ")
    print geo_results['results'][0]['geometry']['location']['lng']

def distanceFrom(origins, destinations, mode): 
    distance_url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&sensor=false&mode=%s&units=imperial"%(origins, destinations, mode)
    maps_request = urllib.urlopen(distance_url)
    result = json.loads(maps_request.read())
    print "\n The distance between %s and %s is" % (original, destination)
    print result['rows'][0]['elements'][0]['distance']['text']

def durationTo(origins, destinations, mode): 
    distance_url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&sensor=false&mode=%s&units=imperial"%(origins, destinations, mode)
    maps_request = urllib.urlopen(distance_url)
    result = json.loads(maps_request.read())
    print "\n The time it takes to travel  between %s and %s is" % (original, destination)
    print result['rows'][0]['elements'][0]['duration']['text']

original = "345 Chambers Street"
destination = "97 Warren Street"
#somehow we have to restrict the modes they can choose from. cause certain inputs like "walking" "driving" and "car" (i believe) work, but "foot" doesn't. so maybe do a dropdown menu somewhere in utils/app.py. i'll change the variable values once we have a more solid thing to work off of
m = "walking" 
getAddress(original)
getLatLong(original)
distanceFrom(original, destination, m)
durationTo(original, destination, m)


