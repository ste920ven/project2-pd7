import utils
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app = Flask(__name__)
key = "AIzaSyDm3LFbtgPrB8jtcruyGlf9ED-tidYvYrA"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        foodname = request.form['foodname']
        return findprice(foodname)
    else:
        return render_template("index.html")

@app.route("/findprice", methods = ["GET", "POST"])
def findprice(foodname):
    searchURL = utils.search(foodname)
    recipeTitle = utils.recipeName(searchURL)
    ingred= utils.ingredients(searchURL)
    imgURL= utils.getImage(searchURL)
    directions= utils.getDirections(searchURL)
    t = 0.0

    pricelist=[]
    for ingredient in ingred:
        p, n = utils.getPrice(key, ingredient)
        t += p;
        p = str(p);
        if len(p[p.find('.'):]) < 3:
            p += '0'
        #sometimes the price shows up with 1 decimal place. I'm assuming it lopped off a 0 somehow.
        pListelement = [p, (n.replace("#food", "") + " (" + ingredient) + ")"]
        #getting #food in the ingredient names was a problem
        pricelist.append(pListelement)
    return render_template("pricer.html", foodname=foodname, title=recipeTitle, sURL=searchURL, ingredients=ingred,imgURL=imgURL, prices=pricelist, total=t,directions=directions)

@app.route("/back", methods = ["GET", "POST"])
def back():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True, port=7203)
    
