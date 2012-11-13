import json
import urllib
from bs4 import BeautifulSoup

#place/nearbysearch location=-33.8670522,151.1957362&radius=500

def test(address, tag):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(address)
    maps_request = urllib.urlopen(geocode_url)
    geo_results = json.loads(maps_request.read())
    print("\n google maps: ")
    print geo_results['results'][0]['formatted_address']
    print("\n")

a = "345 Chambers Street, New York"
t = "park"
test(a, t)
