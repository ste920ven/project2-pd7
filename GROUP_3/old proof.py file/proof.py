import urllib2
from bs4 import BeautifulSoup
import json

key = 'AIzaSyDm3LFbtgPrB8jtcruyGlf9ED-tidYvYrA'

def search(food):
    """
    Returns the first item on the search list of that food
    """
    l = food.split()
    d = ""
    for item in l:
        if item != l[len(l)-1]:
            d = d + item + "%20"
        else:
            d = d + item    

    searchu = "http://allrecipes.com/search/default.aspx?qt=k&wt=%s&rt=r&origin=Recipe%%20Search%%20Results"%(d)

    soup = BeautifulSoup(urllib2.urlopen(searchu).read())
    a = soup.findAll(True,{'id':"ctl00_CenterColumnPlaceHolder_rptResults_ctl00_ucResultContainer_ucRecipe_lnkImage"})
    return a[0].attrs['href']

def recipeName(url):
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    a = soup.findAll(True, {"id":"itemTitle"})
    name = a[0].string
    return name

def ingredients(recipe):
    """
    Gets a list of all the ingredients in any given recipe
    """
    soup = BeautifulSoup(urllib2.urlopen(recipe).read())
    
    a = soup.findAll(True, {'class':"ingredient-name"})
    b = []
    for item in a:
        try:
            b.append(str(item.contents[0]))
        except:
            pass
    return b

def getImage(url):
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    a = soup.findAll(True, {'id':"metaOpenGraphImage"})
    return a[0].attrs['content']


"""
print ingredients('http://allrecipes.com/recipe/brownie-frosting/detail.aspx?event8=1&prop24=SR_Title&e11=brownies&e8=Quick%20Search&event10=1&e7=Home%20Page')
I removed the unneccessary parameters from the URL to make it easier to use
with future code, but I'll keep the long one commented in case we need it
in the future. -Brian
"""

def getPrice(k,name):
    name = name + "+food"
    name=urllib2.quote(name)
    url2 = 'https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=%s'%(k,name)
    request = urllib2.urlopen(url2)
    result2 = json.loads(request.read())
    price = result2['items'][0]['product']['inventories'][0]['price']
    name = result2['items'][0]['product']['title']
    #print str(name) + " " + str(price)
    return  (str(name),str(price))


def prices(l,name,k):
    recipe = {'name':name,'gredients':[]}
    for item in l:
        
        founditem,price=getPrice(k,item)
        recipe['gredients'].append( (item,founditem,price))
    return recipe


#print ingredients(search("lemon merengue pie stuff"))
#recipeName(search("lemon merengue pie"))
rr = search("lemon merengue pie")

prices(ingredients(rr),recipeName(rr),key)

der = search("orange")
getImage(der)
