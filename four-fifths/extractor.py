from bs4 import BeautifulSoup
import urllib2

home = BeautifulSoup(urllib2.urlopen("http://stuy.enschool.org/").read())
news = home.table.find_all("td",id="r")
scheduleurl = "http://stuy.enschool.org" + home.find("a",text="Weekly Schedule")['href']

schedule = BeautifulSoup(urllib2.urlopen(scheduleurl).read()).find(class_="content")

#remove all the img, link, span, br, b tags
i = len(schedule.find_all(["img","link","span","br","b"]))
for x in xrange(0,i):
    schedule.find(["img","link","span","br","b"]).unwrap()

#remove the fbList
schedule.find("ul",class_="fbList").extract()

#remove the pageTitle
schedule.find("div",class_="pageTitle").extract()

#remove the calendar links
schedule.find("a",text="Calendar View").extract()
schedule.find("a",text="Monthly View").extract()

#remove the >> (&raquo;) characters
schedule = BeautifulSoup(schedule.prettify().replace(unicode(u"\u00BB"),""))

#make the wrapper div have an id of schedule instead of a class of content
del schedule.div['class']
schedule.div['id'] = "schedule"

##################################################################

print schedule.prettify()

'''
print "NEWS"
for entry in news:
    print entry.prettify()
'''
