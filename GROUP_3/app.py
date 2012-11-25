import utils
from flask import Flask
from flask import request
from flask import render_template

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

    pricelist=[]
    for ingredient in ingred:
        pricelist.append(str(utils.getPrice(key, ingredient))+ " for " + ingredient)
    return render_template("pricer.html", foodname=foodname, title=recipeTitle, sURL=searchURL, ingredients=ingred,imgURL=imgURL, prices=pricelist)

@app.route("/back", methods = ["GET", "POST"])
def back():
    return home()

if __name__ == '__main__':
    app.run(debug = True)
