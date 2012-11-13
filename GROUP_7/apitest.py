import json
import urllib
from bs4 import BeautifulSoup

#place/nearbysearch location=-33.8670522,151.1957362&radius=500

def test(address):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(address)
    maps_request = urllib.urlopen(geocode_url)
    geo_results = json.loads(maps_request.read())
    print("\n google maps: ")
    print geo_results['results'][0]['formatted_address']
    print("\n")

a = "345 Chambers Street, New York"
test(a)


def test2(loc,radius,key,tag):
    google_maps_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&sensor=false&key=%s&types=%s"%(loc,radius,key,tag)
    maps_request = urllib.urlopen(google_maps_url)
    result = json.loads(maps_request.read())
    print result['results']

key='AIzaSyCM_M56XMiApQyGP8gYGVafJmix15AcUng'
loc="-33.8670522,151.1957362"
radius="300"
tag="park"

test2(loc,radius,key,tag)


