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

#a header to tell reddit what I'm doing
headers = { 'user-agent': '/u/ SandyDamage collect images of hurricane sandy'}

#start session and pass data
client = requests.session()
r = client.post(r'http://www.reddit.com/api/login', data = user_pass_dict)

#save cookie info
j =  json.loads(r.text)
client.modhash = j['json']['data']['modhash']

#this gets the json data from when you search sandy in reddit
url = 'http://www.reddit.com/search.json?q=sandy'
request = urllib.urlopen(url)
results = json.loads(request.read())


def image_crawl(num):
    i = 0
    url_list = []
    while (i < num):
        #stringIO allows for manipulation of strings
        io = StringIO()
        #this dumps the JSON data into a string
        try:

            json.dump(results['data']['children'][i]['data']['url'], io)
        #this makes sure it's an imgur link that isn't an album
            if ('imgur' in io.getvalue() and '#' not in io.getvalue() and '/a/' not in io.getvalue() ):
            #get rid of extra quotes 
                url_list.append(io.getvalue().strip('"'))

        except KeyError:
            print "KeyError"

        except:
            #print results['data']['children'][i]['data']['url']
            print sys.exc_info()[0]
  
        i = i + 1        
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
    print newlist
    print y

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

send_image_links(40)
