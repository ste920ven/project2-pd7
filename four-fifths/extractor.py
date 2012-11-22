from bs4 import BeautifulSoup
import urllib2,html5lib
import datetime

def loadStuySite():
    home = BeautifulSoup(urllib2.urlopen("http://stuy.enschool.org/").read(),"html5lib")
    scheduleurl = "http://stuy.enschool.org" + home.find("a",text="Weekly Schedule")['href']
    schedule = BeautifulSoup(urllib2.urlopen(scheduleurl).read()).find(class_="content")
    return [home,schedule,scheduleurl]

def getSchedule(schedule,scheduleurl):

    #remove the pageTitle
    schedule.find("div",class_="pageTitle").extract()

    #remove all the img, link, span, br, hr, b tags
    i = len(schedule.find_all(["img","link","span","br","hr","b"]))
    for x in xrange(0,i):
        schedule.find(["img","link","span","br","hr","b"]).unwrap()

    #remove the div tags with no id
    i = len(schedule.find_all("div",id=False))
    for x in xrange(0,i):
        schedule.find("div",id=False).unwrap()

    #remove the fbList
    schedule.find("ul",class_="fbList").extract()

    #remove the calendar links
    schedule.find("a",text="Calendar View").extract()
    schedule.find("a",text="Monthly View").extract()

    #remove the >> (&raquo;) characters
    schedule = BeautifulSoup(schedule.prettify().replace(unicode(u"\u00BB"),""))

    #make the wrapper div have an id of schedule instead of a class of content
    del schedule.div['class']
    schedule.div['id'] = "schedule"

    #make the words "Weekly Schedule" a link to the stuy site
    schedulestr = schedule.prettify().strip().split('\n')
    schedulestr[1] = '<a href="'+scheduleurl+'">'+schedulestr[1]+'</a>'

    #put br tags after every line
    schedulestr = '<br/>\n'.join(schedulestr)
    return schedulestr.replace('<br/>','',1)

def getNews(home):

    news = home.table.find_all("td",id="r")

    for entry in news:
        #make each td tag into an li tag with no id
        entry.name = "li"
        del entry['id']
        #remove all the br tags
        i = len(entry.find_all("br"))
        for x in xrange(0,i):
            entry.find("br").unwrap()
        #make the links go to the stuy site
        for link in entry.find_all("a",href=True):
            if not("http" in link['href']):
                link['href'] = "http://stuy.enschool.org" + link['href']
        #put br tags after each news item's title link
        entry.find("a",href=True).insert_after(home.new_tag("br"))
        entry = entry.prettify()
    return news

def getDate():
    return datetime.datetime.today().strftime("%A, %B %e")    

#returns a string with one of the following: regular, homeroom, special, conference, closed or unknown.
def getBellDay(schedule):
    month = datetime.datetime.today().strftime("%b")
    day   = datetime.date.today().day
    found = False
    for line in schedule.split('<br/>'):
        if found==True:
            if "REGULAR"    in line.upper(): return "Regular"
            if "HOMEROOM"   in line.upper(): return "Homeroom"
            if "SPECIAL"    in line.upper(): return "Special"
            if "CONFERENCE" in line.upper(): return "Conference"
            if "CLOSED"     in line.upper(): return "Closed"
            if datetime.datetime.today().weekday()>4: return "Weekend"
            else:                            return "Unknown"
        if (month.upper() in line.upper()) and (str(day) in line): found = True
    if found==False: return "unknown"

def getGymDay(schedule):
    month = datetime.datetime.today().strftime("%b")
    day   = datetime.date.today().day
    lines = schedule.split('<br/>')
    for i in range(len(lines)):
        if (month.upper() in lines[i].upper()) and (str(day) in lines[i]):
            if i+2<len(lines):
                if 'A' in lines[i+2]:
                    if 'A1' in lines[i+2] : return 'A1'
                    if 'A2' in lines[i+2] : return 'A2'
                    else : return 'A'
                if 'B' in lines[i+2]:
                    if 'B1' in lines[i+2] : return 'B1'
                    if 'B2' in lines[i+2] : return 'B2'
                    else : return 'B'
    return "unknown"
