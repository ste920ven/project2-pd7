from flask import Flask, request, redirect, render_template, session,url_for,flash
import twilio.twiml
import factual_search
import urllib2
import math

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def sendSMS():
    text = request.values.get('Body', None)
    try:
        result = factual_search.getSearchString(text)
    except:
        result = ""
    resp = twilio.twiml.Response()
    resp.sms(result)
    #resp.sms("Hello")
    return index()

def index():
    if request.method == 'POST':
        num = request.form['number']
        url=urllib2.quote('/rates/%s'%(num))
        return redirect(url)
    #print twilio_records.getRecords(num)
    return render_template('index.html')

@app.route("/rates/<num>", methods = ['GET', 'POST'])
def rates(num):
    ratings = {"toast":"This restaurant has a good burger", "abbey": "Great atmosphere", "five guys": "Two Patties!"}
    return render_template('restaurants.html', numb = num, ratings = ratings )

@app.route("/getrating/<num>/<name>", methods = ['GET', 'POST'])
def getrating(num, name):
    ratings = {"toast":"This restaurant has a good burger", "abbey": "Great atmosphere", "five guys": "Two Patties!"}
    return ratings[name]

 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7201, debug=True)
