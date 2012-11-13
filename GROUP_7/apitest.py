import json
import urllib
from bs4 import BeautifulSoup

google_maps_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&sensor=false&key=AIzaSyCM_M56XMiApQyGP8gYGVafJmix15AcUng"

def test():
    maps_request = urllib.urlopen(google_maps_url).read()
    soup = BeautifulSoup(maps_request)
    print("google maps: \n")
    print soup

test()
