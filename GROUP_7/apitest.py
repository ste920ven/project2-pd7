import json
import urllib
from bs4 import BeautifulSoup

#place/nearbysearch location=-33.8670522,151.1957362&radius=500

def test(address):
    google_maps_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(address)
    maps_request = urllib.urlopen(google_maps_url)
    results = json.loads(maps_request.read())
    print("google maps: \n")
    print results['results'][0]['formatted_address']
a = "722 East 22nd Street, Brooklyn"
test(a)
