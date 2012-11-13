import json
import urllib

def test():
    request = urllib.urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&sensor=false&key=AIzaSyCM_M56XMiApQyGP8gYGVafJmix15AcUng")
    result = json.load(request.read())
    print result

test()
