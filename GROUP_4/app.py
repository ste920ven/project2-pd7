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
    print "woo"
    if request.method == "GET":
        print "woo2"
        button = request.form["button"]
        return render_template("survey.html")
    else:
        return render_template("survey.html")
        print "fucking a"
    
        #if button == "SAVE!!!":
            #blah
        #r1 = request.form['question1']
        #r2 = request.form['question2']
        #send1 = ["Hello Testing Hello", "TEST ! @ #"]
        #return render_template("results.html",list1 = send1)
    #print "wooo"
@app.route("/results",methods=["GET","POST"])
def results():
    return render_template("survey.html") ##this template doesnt exist yet

if __name__ == "__main__":
    app.run(debug = True)
