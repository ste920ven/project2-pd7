import urllib2, json, sys
from bs4 import BeautifulSoup

key = 'AIzaSyDm3LFbtgPrB8jtcruyGlf9ED-tidYvYrA'

def search(food):
    """
    Returns the first item on the search list of that food
    I went through the extra hassle of using mobile.allrecipes.com because its webpages are much lighter. It looks like our program runs much faster too, from about 3.5 seconds to load the recipe to 1.25 seconds!
    """
    l = food.split()
    d = ""
    for item in l:
        if item != l[len(l)-1]:
            d = d + item + "%20"
        else:
            d = d + item    
    #print ("http://allrecipes.com/search/default.aspx?qt=k&wt=%s&rt=r&origin=Recipe%%20Search%%20Results"%(d))
    #searchu = "http://allrecipes.com/search/default.aspx?qt=k&wt=%s&rt=r&origin=Recipe%%20Search%%20Results"%(d)

    searchu = "http://mobile.allrecipes.com/search/recipes?wt=%s"%(d)

    soup = BeautifulSoup(urllib2.urlopen(searchu).read())
    a = soup.find(True,{'class':"jqRecipeListItem rec-list-view bdr-dotted template-margin"})
    toreturn = []
    searchURL = "http://mobile.allrecipes.com/recipe/"+a.attrs["data-recipeid"]+"/"+a.attrs["data-title"]
    soup = BeautifulSoup(urllib2.urlopen(searchURL).read())
    a = soup.find(True, {"class":"rec-image-thumb rec-shadow"})
    name = a.attrs["alt"]
    toreturn.append(name)

    a = soup.findAll(True, {'class':"recipe-ingred_txt"})
    b = []
    for item in a:
        try:
            temp = str(item.contents[0])
            if temp == 'water':
                continue
            else:
                if temp.find(')') > -1:
                    q, w, temp = temp.partition(')')
                else:
                    temp= temp[temp.find(' ', temp.find(' ') + 1)+1:]
                b.append(temp)
                print temp
        except:
            pass
    toreturn.append(b)

    #gets image of the food
    a = soup.find(True, {'class':"rec-image-thumb rec-shadow"})
    imglink = a.attrs['src']
    toreturn.append(imglink.replace('140x140','250x250',1))

    a = soup.findAll('ol')
    b = a[0].findAll('li')
    c = []
    for item in b:
        c.append(item.string)
    toreturn.append(c)
    toreturn.append(searchURL)
    return toreturn

def getPrice(k,name):
    name = name + "+food"
    name=urllib2.quote(name)
    url2 = 'https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&tbs=cat:422&q=%s'%(k,name)
    request = urllib2.urlopen(url2)
    result2 = json.loads(request.read())
    #provisional nonsense to get around the error that happens with some foods that DO return recipes, like calamari
    try:
        price = result2['items'][0]['product']['inventories'][0]['price']
        name = result2['items'][0]['product']['title']
        return price, str(name)
    except:
        #sys.exit("No, no, is no work")
        #maybe replace this with an error page?
        return None, None 

def prices(l,name,k):
    recipe = {'name':name,'gredients':[]}
    for item in l:
        founditem,price =getPrice(k,item)
        recipe['gredients'].append( (item, founditem, price))
    return recipe


