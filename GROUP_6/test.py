import json
import urllib2

url = 'http://www.reddit.com/search.json?q=sandy'
request = urllib2.urlopen(url)
result = json.loads(request.read())

for i in result['data']:
    print i['thumbnail']


