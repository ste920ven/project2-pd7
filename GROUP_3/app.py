import utils
import time
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import flash

app = Flask(__name__)
app.secret_key="blah"
key = "AIzaSyDm3LFbtgPrB8jtcruyGlf9ED-tidYvYrA"
fail = False
food = ""

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        foodname = request.form['foodname']
        return findprice(foodname, 0)
    else:
        return render_template("index.html", fail=fail)

@app.route("/findprice", methods = ["GET", "POST"])
def findprice(foodname, mode):
    global food
    print "foodname: " + foodname
    print "Times (in ms):\n"
        
        #timer for debugging
    one=time.time()*1000.0
        
    if mode == 0:
        results = utils.search(foodname)
    else:
        results = utils.search2(foodname)

    print "Total recipe search: " + str(time.time()*1000.0 - one)

    #the time for the following assignments is negligible
    recipeTitle = results[0]
    ingred = results[1]
    imgURL = results [2]
    directions = results[3]
    source = results[4]

    #timer 2
    two=time.time()*1000.0
        
    pricelist=[]
    for ingredient in ingred:
        p,n = utils.getPrice(key, ingredient)
        if p == None:
            flash("Your search has failed.  Please try another recipe.")
            return redirect('/')
        p = str(p);
        if len(p[p.find('.'):]) < 3:
            p += '0'
        #sometimes the price shows up with 1 decimal place. I'm assuming it lopped off a 0 somehow.
        pListelement = [p, (n.replace("#food", "") + " (" + ingredient) + ")"]
        #getting '#food' in the ingredient names was a problem
        pricelist.append(pListelement)

    timer = time.time()*1000.0 - two
    print "Total ingredient search: " + str(timer)
    print "   average per ingredient: " + str(timer / len(pricelist))
    print "Total to find data: " + str(time.time()*1000.0 - one)
    food = foodname
    
    return render_template("pricer.html", foodname=foodname, title=recipeTitle, sURL=source, ingredients=ingred,imgURL=imgURL, prices=pricelist, directions=directions)

@app.route("/back", methods = ["GET", "POST"])
def back():
    return redirect('/')

@app.route("/tryagain", methods = ["GET", "POST"])
def tryagain():
    return findprice(food, 1)

if __name__ == '__main__':
    app.run(debug = True, port=7203)
    
