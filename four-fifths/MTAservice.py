from bs4 import BeautifulSoup
import urllib2,html5lib

def getStatus():
    soup = BeautifulSoup(urllib2.urlopen("http://www.mta.info/status/serviceStatus.txt").read(),"html5lib")
    #Converts HTML Entities to actual html
    soup = soup.prettify(formatter=None)
    soup = BeautifulSoup(soup)
    #removes markup taken from Zach
    i = len(soup.find_all(["img","link","span","br","hr","b","p"]))
    for x in xrange(0,i):
        soup.find(["img","link","span","br","hr","b","p"]).unwrap()
    return soup

#Gets Subway data
def getSubways():
    soup = getStatus()
    service_tag =soup.service
    subway_tag = soup.subway.extract()
    return subway_tag
    

print getStatus()
print getSubways()

    
    
