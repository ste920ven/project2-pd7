from flask import Flask,url_for,redirect,flash,session,escape,request,render_template
from pymongo import connection
import random
from random import choice
import upcoming
import movies
import login
#import espn


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
        return render_template("survey2.html", username = username)
    else:
        r1 = request.form['zipcode'] ##returns Zipcode
        print r1
        r2 = request.form['select1'] ##returns fav. baseball team
        print r2
        r3 = request.form['Genres'] 
        print r3
        r4 = request.form['Cuisines']
        print r4


        ## API Interactions HERE ##
        s3 = upcoming.getEventInfo(r3,r1,"id")
        x = random.choice(s3.keys())
        name =  upcoming.getEventIDInfo(x,"name")
        description =  upcoming.getEventIDInfo(x,"description")

        movies_available = movies.getMovieNames()
        movie = choice(movies_available)
        synopsis = movies.getSynopsis(movie)

        #teamId = espn.getTeamID(r2)
        #headlines = espn.getTeamNews(teamId)
        
        return render_template("results.html", username = username,name=name,description = description,movie = movie,synopsis = synopsis)

if __name__ == "__main__":
    app.run(debug = True)
