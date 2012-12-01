from flask import Flask,url_for,redirect,flash,session,escape,request,render_template
from pymongo import connection


import login
import espn


app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/",methods=["GET","POST"])
def user():
    global username
    if request.method == "GET":
        return render_template("user.html")

    if request.method == "POST":
        if request.form["button"] == "Submit":
            username = str(request.form['username'])
            print username
            login.newUser(username)
            login.username(username)
            return render_template("user.html")
           # return redirect(url_for('home'))

        if request.form["button"] == "Login":
            username = str(request.form['login'])
            if(login.username(username) != -1):
                return redirect(url_for('home'))
            else:
                return render_template("user.html")



@app.route("/home", methods= ["GET","POST"])
def home():
    global headlines
    if request.method == "GET":
        print "get!!"
        return render_template("survey.html", username = username)
    
    if  button==request.form.get('button',""):
        print "post1"
        if button == 'Save!':
            print "post works!!"
            r1 = request.form.get('zipcode') ##returns Zipcode
            #print r1
            r2 = request.form.get('select1') ##returns fav. baseball team
            teamId = espn.getTeamID(r2)
            headlines = espn.getTeamNews(teamId)
            r3 = request.form['Action']
            print r3
            if r3 == "on":
                ##means it was selected
                return Action
            #return render_template("results.html")
            return render_template("survey.html", username = username)

if __name__ == "__main__":
    app.run(debug = True)
