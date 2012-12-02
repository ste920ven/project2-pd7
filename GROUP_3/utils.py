import urllib2, json, sys
from bs4 import BeautifulSoup

key = 'AIzaSyDm3LFbtgPrB8jtcruyGlf9ED-tidYvYrA'

def search(food):
    """
    Returns the first item on the search list of that food
    Extracts ingredient names less reliably, but is much faster than search2
    """
    l = food.split()
    d = ""
    for item in l:
        if item != l[len(l)-1]:
            d = d + item + "%20"
        else:
            d = d + item    
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
                if temp.find('egg') > -1:
                    temp = temp[temp.find(' ') + 1:]
                    b.append(temp)
                else:
                    if temp.find(')') > -1:
                        q, w, temp = temp.partition(')')
                        temp = temp.lstrip()
                        b.append(temp)
                    else:
                        temp = temp[temp.find(' ', temp.find(' ') + 1) + 1:]
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

def search2(food):
    """
    This version is much (like 2.8 times) slower, but it should get the ingredients more reliably. The non-mobile site splits ingredient items into quantity and name while the mobile one mushes them together, so that version needs a (not-so-good) quantity remover
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
    toreturn = []
    searchURL = a[0].attrs['href']
    soup = BeautifulSoup(urllib2.urlopen(searchURL).read())
    a = soup.findAll(True, {"id":"itemTitle"})
    name = a[0].string
    toreturn.append(name)

    a = soup.findAll(True, {'class':"ingredient-name"})
    b = []
    for item in a:
        try:
            if str(item.contents[0]) != 'water':
                b.append(str(item.contents[0]))
        except:
            pass
    toreturn.append(b)

    a = soup.findAll(True, {'id':"metaOpenGraphImage"})
    toreturn.append(a[0].attrs['content'])

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
    try:
        price = result2['items'][0]['product']['inventories'][0]['price']
        name = result2['items'][0]['product']['title']
        return price, str(name)
    except:
        return None, None 

def prices(l,name,k):
    recipe = {'name':name,'gredients':[]}
    for item in l:
        founditem,price =getPrice(k,item)
        recipe['gredients'].append( (item, founditem, price))
    return recipe


