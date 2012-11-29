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
    lines =  subways.find_all('line')
    return lines

def getBuses():
    soup = getStatus()
    service_tag=soup.service
    buses = soup.bus.extract()
    lines = buses.find_all('line')
    return lines

def getPlannedWork(soup):
    msgs = soup.find(class_="plannedWorkDetailLink")
    return msgs.get_text(strip=True)

def getPlannedWorkDetail(soup):
    msgs = soup.find(class_="plannedWorkDetail")
    return msgs.get_text(strip=True)

def getDelays(soup):
    delays = soup.text.get_text(strip=True)
    return delays

def get123():
    trains = getSubways()
    train123 = trains[0]
    status = str(train123.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "This line is working fine"
    elif(status=="PLANNED WORK"):
        mesg = (str(getPlannedWork(train123))+str(getPlannedWorkDetail(train123)))#doesnt work because this message has dots 
        return mesg
    elif(status=="DELAYS"):
        return "not yet"

def get456():
    trains = getSubways()
    train456=trains[1]
    status = str(train456.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "This line is working fine"
    elif(status=="PLANNED WORK"):
        mesg = (str(getPlannedWork(train456))+str(getPlannedWorkDetail(train456)))
        return mesg
    elif(status=="DELAYS"):
        return "not yet"
        
#print getBuses()
#print get123()
print get456()    


    
    
