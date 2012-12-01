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

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        foodname = request.form['foodname']
        return findprice(foodname)
    else:
        return render_template("index.html", fail=fail)

@app.route("/findprice", methods = ["GET", "POST"])
def findprice(foodname):
    #timer for debugging
    one=time.time()*1000.0

    results = utils.search(foodname)

    #timer 2
    two=time.time()*1000.0

    recipeTitle = results[0]
    ingred = results[1]
    imgURL = results [2]
    directions = results[3]
    source = results[4]

    #timer 3
    three=time.time()*1000.0

    t = 0.0
    pricelist=[]
    for ingredient in ingred:
        p,n = utils.getPrice(key, ingredient)
        if p == None:
            flash("Your search has failed.  Please try another recipe.")
            return redirect('/')
        t += p;
        p = str(p);
        if len(p[p.find('.'):]) < 3:
            p += '0'
        #sometimes the price shows up with 1 decimal place. I'm assuming it lopped off a 0 somehow.
        pListelement = [p, (n.replace("#food", "") + " (" + ingredient) + ")"]
        #getting '#food' in the ingredient names was a problem
        pricelist.append(pListelement)

    four=time.time()*1000.0
    #printing load time to look for bottlenecks in the program, and for science
    print "time to search food: "+str((two-one))+" time to assign some params: "+str((three-two))+" time to populate/price ingredients: "+str((four-three))

    return render_template("pricer.html", foodname=foodname, title=recipeTitle, sURL=source, ingredients=ingred,imgURL=imgURL, prices=pricelist, total=t,directions=directions)

@app.route("/back", methods = ["GET", "POST"])
def back():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True, port=7203)
    
