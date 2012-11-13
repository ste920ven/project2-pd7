import json
import urllib
from bs4 import BeautifulSoup

#place/nearbysearch location=-33.8670522,151.1957362&radius=500

def test(address):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(address)
    maps_request = urllib.urlopen(geocode_url)
    geo_results = json.loads(maps_request.read())
    print("google maps: \n")
    print geo_results['results'][0]['formatted_address']

a = "345 Chambers Street, New York"
test(a)


def test(loc,radius,key):
    google_maps_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%d&radius=%d&sensor=false&key=%s"%(loc,radius,key)
    maps_request = urllib.urlopen(google_maps_url)
    result = json.loads(maps_request.read())
    return result

key='AIzaSyCM_M56XMiApQyGP8gYGVafJmix15AcUng'
loc="-33.8670522,151.1957362"
radius="300"

test(loc,radius,key)

