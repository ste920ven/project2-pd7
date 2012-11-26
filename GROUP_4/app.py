from flask import Flask,url_for,redirect,flash,session,escape,request,render_template
from pymongo import connection
#import espn
#import factual
#import upcoming

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/")
def home():
    return redirect("/survey")

@app.route("/survey", methods=["GET","POST"])
def survey():
    if request.method == "GET":
        return render_template("htmlkickstart-joshuagatcke/survey.html")
    if request.method == "POST":
        #button = request.form["button"]
        #if button == "SAVE!!!":
            #blah
        r1 = request.form['question1']
        #r2 = request.form['question2']
        '''
        AN API METHOD WILL NOW SEARCH USING THE DATA
        GATHERED IN variable r1
        send1 = espn(r1)
        '''
        send1 = ["Hello Testing Hello", "TEST ! @ #"]
        return render_template("results.html",list1 = send1)

@app.route("/results",methods=["GET","POST"])
def results():
    return render_template("survey.html") ##this template doesnt exist yet

if __name__ == "__main__":
    app.run(debug = True)
