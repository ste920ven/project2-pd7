import json
import urllib

url = 'http://www.reddit.com/search.json?q=sandy'
request = urllib.urlopen(url)
results = json.loads(request.read())


print results['data']['children'][0]['data']['url']



