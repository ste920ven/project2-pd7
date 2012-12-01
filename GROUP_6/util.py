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
headers = { 'user-agent': '/u/ SandyDamage collect images of hurricane sandy'}

#start session and pass data
client = requests.session()
r = client.post(r'http://www.reddit.com/api/login', data = user_pass_dict)

#save cookie info
j =  json.loads(r.text)
client.modhash = j['json']['data']['modhash']


url = 'http://www.reddit.com/search.json?q=sandy'
request = urllib.urlopen(url)
results = json.loads(request.read())


def image_crawl(num):
    i = 0
    url_list = []
    while (i < num):
        io = StringIO()
        json.dump(results['data']['children'][i]['data']['url'], io)
        if ('imgur' in io.getvalue() and '#' not in io.getvalue()):
            #url = io.getvalue()
            #url = strip(url
            url_list.append(io.getvalue().strip('"'))
        i = i + 1    
    
    return url_list

def get_image_url(url):
    #if url is already just the image link
    if (url[1] is '.'):
        return url
    else:
        return 'http://www.i.imgur.com/'+url[-9:]
        
x = image_crawl(20)
print x
    
#print results['data']['children'][0]['data']['url']



