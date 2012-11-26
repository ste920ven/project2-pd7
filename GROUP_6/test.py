import json
import requests
import urllib


username = 'SandyDamage'
password = 'stuy123'

user_pass_dict = {'user': username,
                  'passwd': password,
                  'api_type': 'json' }

headers = { 'user-agent': '/u/SandyDamage\'s Hurricane Sandy Image Crawler'}

client = requests.session()
r = client.post(r'http://www.reddit.com/api/login', data = user_pass_dict)

j =  json.loads(r.text)
client.modhash = j['json']['data']['modhash']
url = 'http://www.reddit.com/search.json?q=sandy'
request = urllib.urlopen(url)
results = json.loads(request.read())


print results['data']['children'][0]['data']['url']



