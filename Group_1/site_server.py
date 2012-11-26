from flask import Flask, request, render_template
import math
from flask import session,url_for,redirect,flash
import urllib2

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():

    if request.method == 'POST':
        num = request.form['number']
        url=urllib2.quote('/rates/%s'%(num))
        return redirect(url)
    return render_template('index.html')


@app.route("/rates/<num>", methods = ['GET', 'POST'])
def rates(num):
    return render_template('restaurants.html', numb = num)


if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() # connect to localhost:5000 or http://127.0.0.1:5000
