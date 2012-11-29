from bs4 import BeautifulSoup
import urllib2,html5lib

def getStatus():
    soup = BeautifulSoup(urllib2.urlopen("http://www.mta.info/status/serviceStatus.txt").read(),"html5lib")
    #Converts HTML Entities to actual html
    soup = soup.prettify(formatter=None)
    soup = BeautifulSoup(soup)
    i = len(soup.find_all(["img","link","span","br","hr","b","p"]))
    for x in xrange(0,i):
        soup.find(["img","link","span","br","hr","b","p"]).unwrap()
    return soup

def clean(soup):
    #remove styling tags
    REMOVE_ATTRIBUTES = [
        'lang','language','onmouseover','onmouseout','script','style','font',
        'dir','face','size','color','style','class','width','height','hspace',
        'border','valign','align','background','bgcolor','text','link','vlink',
        'alink','cellpadding','cellspacing']
    for tag in soup.recursiveChildGenerator():
        try:
            tag.attrs =[(key,value) for key,value in tag.attrs
                        if key not in REMOVE_ATTRIBUTES]
        except AttributeError:
            pass
    return soup
 #Gets Subway data
def getSubways():
    soup = getStatus()
    service_tag =soup.service
    subways = soup.subway.extract()
    #return subways
    #lines = subways.line.extract()
    return subways.find_all('line')
    

print getSubways()

    
    
