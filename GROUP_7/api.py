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

#we need a dropdown menu that restricts the facilities the users can choose from. then in util.py include a function that can translate that chosen facility into its encoded input value (which will be inputted as category for the function below)
#this function will return all the facilities in NY that are of the selected category. i'm trying to get it to print out in order of closest to furthest distance away from the user's origin
def getFacilityList(origin,category, mode): 
    facilityList_url = "http://www.nyc.gov/portal/apps/311_contentapi/facilities/%s.json"%(category)
    facilityList_request = urllib.urlopen(facilityList_url)
    facilityList_results = json.loads(facilityList_request.read())
    #facilities = []
    #fac_in_order = []
    #dist_in_order = []
    print facilityList_results['facility_name'] #this won't work?!?!!?! 
    """facilities.append(facilityList_results["facility_name"])
    #for facility in facilities:
        #fac_add = getAddress(facility)
        #distance = distanceFrom(origin, fac_add, mode)
        #dist_in_order.append(distance)
        if len(fac_in_order) == 0: 
            fac_in_order.append(facility)
        else:
            if this.distance > fac_in_order[0].distance:
                fac_in_order.append(facility)
            else:
                for a in fac_in_order:
                    if this.distance <= a.distance:
                        fac_in_order.insert((fac_in_order.index(a)), facility)
    dist_in_order.sort()
    print fac_in_order
    print dist_in_order"""

def isPOI(origins):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(origins)
    maps_request = urllib.urlopen(geocode_url)
    geo_results = json.loads(maps_request.read())
    if(geo_results['results'][0]['types'].count('point_of_interest') == 1):
        return "Yes"
    else:
        return "No"
    

original = "345 Chambers Street"
destination = "97 Warren Street"
poi = "Empire State Building"
#somehow we have to restrict the modes they can choose from. cause certain inputs like "walking" "driving" and "car" (i believe) work, but "foot" doesn't. so maybe do a dropdown menu somewhere in utils/app.py. i'll change the variable values once we have a more solid thing to work off of
m = "walking" 
facility = "Beach"

getAddress(original)
getLatLong(original)
distanceFrom(original, destination, m)
durationTo(original, destination, m)
getFacilityList(facility)
print "\n Is %s a POI? : %s" %(original, isPOI(original))
print "\n Is %s a POI? : %s" %(poi, isPOI(poi))
