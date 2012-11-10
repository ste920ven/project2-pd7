import urllib2
from bs4 import BeautifulSoup

url='http://allrecipes.com/Recipe/Homemade-Mac-and-Cheese/Detail.aspx?src=rotd'

result = urllib2.urlopen(url).read()
soup = BeautifulSoup(result)
#print (soup.prettify())

print soup.findAll(True, {'class':"lblIngAmount"})
