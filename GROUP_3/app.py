from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        #print "cardamom"
        #print request.form['foodname']
        foodname = request.form['foodname']
        return findprice(foodname)
    else:
        return render_template("index.html")

@app.route("/findprice", methods = ["GET", "POST"])
def findprice(foodname):
    print foodname
    return render_template("pricer.html")

if __name__ == '__main__':
    app.run(debug = True)
