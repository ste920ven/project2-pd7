from bs4 import BeautifulSoup
import urllib2,html5lib

def getStatus():
    soup = BeautifulSoup(urllib2.urlopen("http://www.mta.info/status/serviceStatus.txt").read(),"html5lib")
    #Converts HTML Entities
    soup = soup.prettify(formatter=None)
    soup = BeautifulSoup(soup)
    i = len(soup.find_all(["img","link","br","hr","b",]))
    for x in xrange(0,i):
        soup.find(["img","link","br","hr","b",]).unwrap()
    return soup

#Planned Work
def getPlannedWork(soup):
    msgs = soup.find(class_="plannedWorkDetailLink")
    if (msgs == None):
        return ""
    else:
        return msgs.get_text(strip=True)

#Planned Work - Alternate routes
def getPlannedWorkDetail(soup):
    msgs = soup.find(class_="plannedWorkDetail")
    if (msgs == None):
        return ""
    else:
        return msgs.get_text(strip=True)

#Service Changes and Delays
def getServiceChangeAndDelays(soup):
    texts = soup.find("text")
    i = len(texts.find_all(["span","a","div"]))
    for x in xrange(0,i):
        texts.find(["span","a","div"]).decompose()
    return texts.get_text(strip=True)
    #msgs = soup.find_all("p")
    #allmsgs = ""
    #for msg in msgs:
    #    allmsgs= allmsgs + msg.get_text(strip=True)
    #return allmsgs
    #return text

#Combines the Planned Work notice and alternate routes
def getCompletePlannedWork(soup):
    mesg = getPlannedWork(soup) +" "+getPlannedWorkDetail(soup)
    return mesg

#Service Changes and Planned Works
def getComplete(soup):
    soup1 = soup
    soup2 = soup
    mesg = "Planned Detours:"+" "+getCompletePlannedWork(soup2)+"\n"+"Delays&ServiceChanges:"+" "+getServiceChangeAndDelays(soup1)
    return mesg

#Gets all lines with delays 
def getDelays(thelines):
    delayedlines = []
    for line in thelines:
        status = str(line.status.get_text(strip=True))
        if(status=="DELAYS"):
            name = line.find("name")
            name.name = "linenames"
            nname = str(name.get_text(strip=True))
            delayedlines.append(nname)
    return delayedlines

#Get service
def getService(thelines):
    service = {}
    for line in thelines:
        status = str(line.status.get_text(strip=True))
        if(status =="SERVICE CHANGE"):
            name = line.find("name")
            name.name = "linenames"
            nname = str(name.get_text(strip=True))
            msg = str(getServiceChangeAndDelays(line))
            service[nname] = msg
    return service

#Returns matching line with given name
def getLine(lines,lname):
    for line in lines:
        name = line.find("name")
        name.name = "linenames"
        nname =str(name.get_text(strip=True))
        if(lname==nname):
            return line

#Subway
def getSubways():
    soup = getStatus()
    service_tag =soup.service
    subways = soup.subway.extract()
    lines =  subways.find_all('line')
    return lines

#123
def get123():
    trains = getSubways()
    train123 = getLine(trains,"123")
    status = str(train123.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        mesg = (getPlannedWork(train123))+" "+(getPlannedWorkDetail(train123))
        return mesg
    elif(status=="DELAYS"):
        return getComplete(train123)
    elif(status=="SERVICE CHANGE"):
        return getComplete(train123)
#456
def get456():
    trains = getSubways()
    train456=getLine(trains,"456")
    status = str(train456.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        mesg = (getPlannedWork(train456))+(getPlannedWorkDetail(train456))
        return mesg
    elif(status=="DELAYS"):
        return getComplete(train456)
    elif(status=="SERVICE CHANGE"):
        return getComplete(train456)

#7
def get7():
    trains = getSubways()
    train7=getLine(trains,"7")
    status = str(train7.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        mesg = (getPlannedWork(train7))+(getPlannedWorkDetail(train7))
        return mesg
    elif(status=="DELAYS"):
        return getComplete(train7)
    elif(status=="SERVICE CHANGE"):
        return getComplete(train7)

#ACE
def getACE():
    trains = getSubways()
    trainACE=getLine(trains,"ACE")
    status = str(trainACE.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        mesg = (getPlannedWork(trainACE))+(getPlannedWorkDetail(trainACE))
        return mesg
    elif(status=="DELAYS"):
        return getComplete(trainACE)
    elif(status=="SERVICE CHANGE"):
        return getComplete(trainACE)

#BDFM
def getBDFM():
    trains = getSubways()
    trainBDFM=getLine(trains,"BDFM")
    status = str(trainBDFM.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(trainBDFM)
    elif(status=="DELAYS"):
        return getComplete(trainBDFM)
    elif(status=="SERVICE CHANGE"):
        return getComplete(trainBDFM)

#G
def getG():
    trains = getSubways()
    trainG=getLine(trains,"G")
    status = str(trainG.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(trainG)
    elif(status=="DELAYS"):
        return getComplete(trainG)
    elif(status=="SERVICE CHANGE"):
        return getComplete(trainG)

#JZ
def getJZ():
    trains = getSubways()
    trainJZ=getLine(trains,"JZ")
    status = str(trainJZ.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(trainJZ)
    elif(status=="DELAYS"):
        return getComplete(trainJZ)
    elif(status=="SERVICE CHANGE"):
        return getComplete(trainJZ)

#L
def getL():
    trains = getSubways()
    trainL=getLine(trains,"L")
    status = str(trainL.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(trainL)
    elif(status=="DELAYS"):
        return getComplete(trainL)
    elif(status=="SERVICE CHANGE"):
        return getComplete(trainL)

#NQR
def getNQR():
    trains = getSubways()
    trainNQR=getLine(trains,"NQR")
    status = str(trainNQR.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(trainNQR)
    elif(status=="DELAYS"):
        return getComplete(trainNQR)
    elif(status=="SERVICE CHANGE"):
        return getComplete(trainNQR)

#S
def getS():
    trains = getSubways()
    trainS=getLine(trains,"S")
    status = str(trainS.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(trainS)
    elif(status=="DELAYS"):
        return getComplete(trainS)
    elif(status=="SERVICE CHANGE"):
        return getComplete(trainS)
#SIR
def getSIR():
    trains = getSubways()
    trainSIR=getLine(trains,"SIR")
    status = str(trainSIR.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(trainSIR)
    elif(status=="DELAYS"):
        return getComplete(trainSIR)
    elif(status=="SERVICE CHANGE"):
        return getComplete(trainSIR)
#Buses
def getBuses():
    soup = getStatus()
    service_tag=soup.service
    buses = soup.bus.extract()
    lines = buses.find_all('line')
    return lines

#B1-B83
def getB1B83():
    buses=getBuses()
    B1B83 = buses[0]
    status = str(B1B83.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(B1B83)
    elif(status=="DELAYS"):
        return getComplete(B1B83)
    elif(status=="SERVICE CHANGE"):
        return getComplete(B1B83)

#B100-B103
def getB100B103():
    buses=getBuses()
    B100B103 = buses[1]
    status = str(B100B103.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(B100B103)
    elif(status=="DELAYS"):
        return getComplete(B100B103)
    elif(status=="SERVICE CHANGE"):
        return getComplete(B100B103)

#BM1-BM5
def getBM1BM5():
    buses=getBuses()
    BM1BM5 = buses[2]
    status = str(BM1BM5.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(BM1BM5)
    elif(status=="DELAYS"):
        return getComplete(BM1BM5)
    elif(status=="SERVICE CHANGE"):
        return getComplete(BM1BM5)

#Bx1-Bx55
def getBX1BX55():
    buses=getBuses()
    BX1BX55 = buses[3]
    status = str(BX1BX55.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(BX1BX55)
    elif(status=="DELAYS"):
        return getComplete(BX1BX55)
    elif(status=="SERVICE CHANGE"):
        return getComplete(BX1BX55)

#BxM1-BxM18
def getBXM1BXM18():
    buses=getBuses()
    BXM1BXM18= buses[4]
    status = str(BXM1BXM18.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(BXM1BXM18)
    elif(status=="DELAYS"):
        return getComplete(BXM1BXM18)
    elif(status=="SERVICE CHANGE"):
        return getComplete(BXM1BXM18)

#M1-M116
def getM1M116():
    buses=getBuses()
    M1M116= buses[5]
    status = str(M1M116.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(M1M116)
    elif(status=="DELAYS"):
        return getComplete(M1M116)
    elif(status=="SERVICE CHANGE"):
        return getComplete(M1M116)

#Q1-Q113
def getQ1Q113():
    buses=getBuses()
    Q1Q113= buses[6]
    status = str(Q1Q113.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(Q1Q113)
    elif(status=="DELAYS"):
        return getComplete(Q1Q113)
    elif(status=="SERVICE CHANGE"):
        return getComplete(Q1Q113)

#QM1-QM25
def getQM1QM25():
    buses=getBuses()
    QM1QM25= buses[7]
    status = str(QM1QM25.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(QM1QM25)
    elif(status=="DELAYS"):
        return getComplete(QM1QM25)
    elif(status=="SERVICE CHANGE"):
        return getComplete(QM1QM25)

#S40-S98
def getS40S98():
    buses=getBuses()
    S40S98 = buses[8]
    status = str(S40S98.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(S40S98)
    elif(status=="DELAYS"):
        return getComplete(S40S98)
    elif(status=="SERVICE CHANGE"):
        return getComplete(S40S98)

#x1-x68
def getX1X68():
    buses=getBuses()
    X1X68 = buses[9]
    status = str(X1X68.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(X1X68)
    elif(status=="DELAYS"):
        return getComplete(X1X68)
    elif(status=="SERVICE CHANGE"):
        return getComplete(X1X68)

#LIRR
def getLIRR():
    soup = getStatus()
    service_tag =soup.service
    lirr = soup.lirr.extract()
    lines =  lirr.find_all('line')
    return lines

#City Terminal Zone
def getCTZ():
    rails=getLIRR()
    CTZ =rails[0]
    status = str(CTZ.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(CTZ)
    elif(status=="DELAYS"):
        return getComplete(CTZ)
    elif(status=="SERVICE CHANGE"):
        return getComplete(CTZ)

#Babylon
def getBaby():
    rails=getLIRR()
    Baby =rails[1]
    status = str(Baby.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(Baby)
    elif(status=="DELAYS"):
        return getComplete(Baby)
    elif(status=="SERVICE CHANGE"):
        return getComplete(Baby)

#Far Rockaway
def getFR():
    rails=getLIRR()
    FR =rails[2]
    status = str(FR.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(FR)
    elif(status=="DELAYS"):
        return getComplete(FR)
    elif(status=="SERVICE CHANGE"):
        return getComplete(FR)

#Hempstead
def getHemp():
    rails=getLIRR()
    Hemp=rails[3]
    status = str(Hemp.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(Hemp)
    elif(status=="DELAYS"):
        return getComplete(Hemp)
    elif(status=="SERVICE CHANGE"):
        return getComplete(Hemp)

#Long Beach
def getLB():
    rails=getLIRR()
    LB =rails[4]
    status = str(LB.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(LB)
    elif(status=="DELAYS"):
        return getComplete(LB)
    elif(status=="SERVICE CHANGE"):
        return getComplete(LB)

#Montauk
def getMontauk():
    rails=getLIRR()
    mon =rails[5]
    status = str(mon.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(mon)
    elif(status=="DELAYS"):
        return getComplete(mon)
    elif(status=="SERVICE CHANGE"):
        return getComplete(mon)

#Oyster Bay
def getOB():
    rails=getLIRR()
    OB =rails[6]
    status = str(OB.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(OB)
    elif(status=="DELAYS"):
        return getComplete(OB)
    elif(status=="SERVICE CHANGE"):
        return getComplete(OB)

#Port Jefferson
def getPortJ():
    rails=getLIRR()
    j =rails[7]
    status = str(j.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(j)
    elif(status=="DELAYS"):
        return getComplete(j)
    elif(status=="SERVICE CHANGE"):
        return getComplete(j)

#Port Washington
def getPortW():
    rails=getLIRR()
    w =rails[8]
    status = str(w.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(w)
    elif(status=="DELAYS"):
        return getComplete(w)
    elif(status=="SERVICE CHANGE"):
        return getComplete(w)

#Ronkonkoma
def getRonkonkoma():
    rails=getLIRR()
    RKK =rails[5]
    status = str(RKK.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(RKK)
    elif(status=="DELAYS"):
        return getComplete(RKK)
    elif(status=="SERVICE CHANGE"):
        return getComplete(RKK)

#West Hempstead
def getWHemp():
    rails=getLIRR()
    wh =rails[5]
    status = str(wh.status.get_text(strip=True))
    if(status=="GOOD SERVICE"):
        return "Good Service"
    elif(status=="PLANNED WORK"):
        return getCompletePlannedWork(wh)
    elif(status=="DELAYS"):
        return getComplete(wh)
    elif(status=="SERVICE CHANGE"):
        return getComplete(wh)

#print getSubways()
#print get123()
#print get456()
#print get7()
#print getACE()
#print getBDFM()
#print getG()
#print getJZ()
#print getL()
#print getNQR()
#print getS()
#print getSIR()  
#print getBuses()
#print getB1B83()
#print getB100B103()
#print getBM1BM5()
#print getBX1BX55()
#print getBXM1BXM18()
#print getM1M116()
#print getQ1Q113()
#print getQM1QM25()
#print getS40S98()
#print getX1X68()
#print getLIRR()
#print getCTZ()
#print getBaby()
#print getFR()
#print getHemp()
#print getLB()
#print getMontauk()
#print getOB()
#print getPortJ()
#print getPortW()
#print getRonkonkoma()
#print getWHemp()
#print getDelays(getBuses())
#print getDelays(getSubways())
#print getDelays(getLIRR())
#print getService(getBuses())
#print getService(getSubways())
#print getService(getLIRR())
print getServiceChangeAndDelays(getLine(getSubways(),"123"))
print getLine(getSubways(),"123")
#print x.find("text")
#print getPlannedWork(getLine(getSubways(),"123"))
#print getCompletePlannedWork(getLine(getSubways(),"123"))
#print getComplete(getLine(getSubways(),"123"))
    
    
