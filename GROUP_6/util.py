import sys
import json
import requests
import urllib
import shutil
import os
from StringIO import StringIO

#this is to login to the reddit API
username = 'SandyDamage'
password = 'stuy123'

#this is what's passed on to the API later
user_pass_dict = {'user': username,
                  'passwd': password,
                  'api_type': 'json' }


urlblock =['http://www.reddit.com/r/sandy/search.json?q=sandy&sort=relevance&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?q=sandy&sort=relevance&after=t3_12kaen&restrict_sr=on&count=25',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=50&after=t3_12a94y&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=100&after=t3_12g8dd&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=125&after=t3_12jwc2&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=150&after=t3_12bfaq&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=175&after=t3_12azsc&q=sandy&restrict_sr=on',
'http://www..reddit.com/r/sandy/search.json?sort=relevance&count=200&after=t3_12bpf2&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=225&after=t3_12cwmu&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=250&after=t3_12b74c&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=275&after=t3_12a9r5&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=300&after=t3_12b0lb&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=325&after=t3_12b02z&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=350&after=t3_12baf5&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=375&after=t3_12bx2t&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=400&after=t3_12bdsx&q=sandy&restrict_sr=on',
'http://www.reddit.com/r/sandy/search.json?sort=relevance&count=425&after=t3_12fvdh&q=sandy&restrict_sr=on']

#a header to tell reddit what I'm doing
headers = { 'user-agent': '/u/ SandyDamage collect images of hurricane sandy'}

#start session and pass data
client = requests.session()
r = client.post(r'http://www.reddit.com/api/login', data = user_pass_dict)

#save cookie info
j =  json.loads(r.text)
client.modhash = j['json']['data']['modhash']

#this gets the json data from when you search sandy in reddit
page = 0
url = urlblock[1] 
request = urllib.urlopen(url)
results = json.loads(request.read())

def next_page(page):
    try:
        url = urlblock[page+1]
    except:
        print "next_page failure"

    request = urllib.urlopen(url)
    results = json.loads(request.read())

def image_crawl(num):
    x = 0
    url_list = []
    while (x < num):
        for i in results['data']['children']:
            iurl = i['data']['url']

        #stringIO allows fo manipulation of strings
            io = StringIO()
        #this dumps the JSON data into a string
            try:

                json.dump(iurl, io)
        #this makes sure it's an imgur link that isn't an album
                if ('imgur' in io.getvalue() and '#' not in io.getvalue() and '/a/' not in io.getvalue() ):
            #get rid of extra quotes 
                    url_list.append(io.getvalue().strip('"'))
                    x = x + 1
            except KeyError:
                print "KeyError"

            except:
            #print results['data']['children'][i]['data']['url']
                print sys.exc_info()[0]
                next_page(page)
    

               
    return url_list


def get_image_url(url): 
   
#if url is already just the image link
    if ('i.imgur' in url):
        return url
    else:
        #this returns the parameters for retrieving an image.
        return 'http://www.i.imgur.com/'+url[-5:]+'.jpg'

        
'''
def save_image(url):    
    #create image space
    image = urllib.URLopener()
    url,filename = get_image_url(url)
    print url
    print filename
    #download file into home directory.
    try:
        print "saving"
        image.retrieve(url,filename)    
    #copy image from current directory where it got saved into the images folder
       src = os.getcwd()+'/'+filename
       dst = os.getcwd()+'/images/'
       shutil.move(src,dst)

    except IOError:
        print "value error not saved"
'''



def download_images(num):
        url_list = []
        url_list = image_crawl(num)    
        
        for i in url_list:
            try:
                print i
                save_image(i)
            except KeyError:
                print "reddit says no"
            except:
                print "huh?"


def send_image_links(num):
    y = 0
    url_list = image_crawl(num)
    newlist = []
    #print test
    for i in url_list:
        x = get_image_url(i)
        #print x
        y = y +1
        newlist.append(x)
    return newlist

#send_image_links(10)
#download_images(10)

#save_image('http://i.imgur.com/Jxyof.jpg')


#x = get_image_url('http://imgur.com/qepuC')
#print x
#print results['data']['children'][20]['data']['url']
'''
x = image_crawl(50)
print x
for i in x:
    i = get_image_url(i)
print x
'''


xx = send_image_links(50)
print xx
#incoming block of links
