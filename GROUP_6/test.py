import json
import requests
import urllib
from StringIO import StringIO

#this is to login to the reddit API
username = 'SandyDamage'
password = 'stuy123'

#this is what's passed on to the API later
user_pass_dict = {'user': username,
                  'passwd': password,
                  'api_type': 'json' }

#a header to tell reddit what I'm doing
headers = { 'user-agent': 'test.py'}

#start session and pass data
client = requests.session()
r = client.post(r'http://www.reddit.com/api/login', data = user_pass_dict)

#save cookie info(?)
j =  json.loads(r.text)
client.modhash = j['json']['data']['modhash']

url = 'http://www.reddit.com/search.json?q=sandy'
request = urllib.urlopen(url)
results = json.loads(request.read())



i = 0
while (i < 20):
    io = StringIO()
    json.dump(results['data']['children'][i]['data']['url'], io)
    if ('imgur' in io.getvalue()):
        print io.getvalue()+"\n"
        

    i = i+1
    
print results['data']['children'][0]['data']['url']



