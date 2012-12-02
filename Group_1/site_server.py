from flask import Flask, request, render_template
import math
from flask import session,url_for,redirect,flash
import urllib2


import twilio_records


#global ratings

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():

    if request.method == 'POST':
        num = request.form['number']
        url=urllib2.quote('/rates/%s'%(num))
        return redirect(url)
    #print twilio_records.getRecords(num)
    return render_template('index.html')


@app.route("/rates/<num>", methods = ['GET', 'POST'])
def rates(num):
    global ratings
    ratings = twilio_records.get_records("+1" + str(num))
    #ratings = {"toast":"This restaurant has a good burger", "abbey": "Great atmosphere", "five guys": "Two Patties!"}
    return render_template('restaurants.html', numb = num, ratings = ratings )

@app.route("/getrating/<num>/<name>", methods = ['GET', 'POST'])
def getrating(num, name):
    #ratings = {"toast":"This restaurant has a good burger", "abbey": "Great atmosphere", "five guys": "Two Patties!"}
    return str(ratings[name])

# @app.route("/ratesimages/preload.gif")
# def preload():
#     return render_template('preload.html')
    


if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() # connect to localhost:5000 or http://127.0.0.1:5000
