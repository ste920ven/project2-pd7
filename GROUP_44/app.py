from flask import Flask,url_for,redirect,flash,session,escape,request,render_template
from pymongo import connection
import random
from random import choice
import upcoming
import movies
import login
import espn


app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/help",methods=["GET","POST"])
def help():
    return render_template("help.html")

@app.route("/about",methods=["GET","POST"])
def about():
    return render_template("about.html")

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
            return redirect(url_for('home'))

        if request.form["button"] == "Login":
            username = str(request.form['login'])
            if(login.username(username) != -1):
                r1 = login.getZip(username)
                r2 = login.getTeamID(username)
                r3 = login.getGenre(username)
                r4 = login.getCategory(username)
                
                try:
                    s3 = upcoming.getEventInfo(r3,r1,"id")
                    x = random.choice(s3.keys())
                    uname1 =  upcoming.getEventIDInfo(x,"name")
                    udescription1 =  upcoming.getEventIDInfo(x,"description")
                except:
                    uname1 = " "
                    udescription1 = " "
                    
                try:
                    s4 = upcoming.getEventInfo(r4,r1,"id")
                    y = random.choice(s4.keys())
                    uname2 =  upcoming.getEventIDInfo(y,"name")
                    udescription2 =  upcoming.getEventIDInfo(y,"description")
                except:
                    uname2 = " "
                    udescription2 = " "
        
        
                    movies_available = movies.getMovieNames()
                    movie = choice(movies_available)
                    print movie
                    synopsis = movies.getSynopsis(movie)
                    print synopsis
        #teamId = espn.getTeamID(r2)
                try:
                    teamId = login.getTeamID(username)
                    headline1 = espn.getHeadline(teamId, 0)
                    headline2 = espn.getHeadline(teamId, 1)
                    headline3 = espn.getHeadline(teamId, 2)
                    description1 = espn.getDescription(teamId, 0)
                    description2 = espn.getDescription(teamId, 1)
                    description3 = espn.getDescription(teamId, 2)
        #team = espn.getName(espn.getTeam(teamId))

                except:
                    headline1 = ""
                    headline2 = ""
                    headline3 = ""
                    description1 = " "
                    description2 = "ESPN API is down. Try again later"
                    description3 = " " 
                    

    
                
                render_template("results.html", 
                                username = username,
                                name=uname1,
                                description = udescription1,
                                movie = movie,
                                #team = team,
                                synopsis = synopsis, 
                                headline1 = headline1,
                                headline2 = headline2,
                                headline3 = headline3,
                                description1 = description1,
                                description2 = description2,
                                description3 = description3,
                                name2 = uname2,
                                udescription2 = udescription2)





@app.route("/home", methods= ["GET","POST"])
def home():
    global headlines
    global username
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
        r4 = request.form['Categories']
        print r4

##Saving Team preferences using mongo ##
        login.saveZip(username, r1)
        login.saveTeamID(username, r2)
        login.saveMusic(username, r3)
        login.saveMood(username, r4)

        login.test(username)


        ## API Interactions HERE ##
        try:
            s3 = upcoming.getEventInfo(r3,r1,"id")
            x = random.choice(s3.keys())
            uname1 =  upcoming.getEventIDInfo(x,"name")
            udescription1 =  upcoming.getEventIDInfo(x,"description")
        except:
            uname1 = " "
            udescription1 = " "

        try:
            s4 = upcoming.getEventInfo(r4,r1,"id")
            y = random.choice(s4.keys())
            uname2 =  upcoming.getEventIDInfo(y,"name")
            udescription2 =  upcoming.getEventIDInfo(y,"description")
        except:
            uname2 = " "
            udescription2 = " "
        
        
        movies_available = movies.getMovieNames()
        movie = choice(movies_available)
        print movie
        synopsis = movies.getSynopsis(movie)
        print synopsis
        #teamId = espn.getTeamID(r2)
        description1 = " "
        description2 = "ESPN API is down. Try again later"
        description3 = " " 
        try:
            teamId = login.getTeamID(username)
            headline1 = espn.getHeadline(teamId, 0)
            headline2 = espn.getHeadline(teamId, 1)
            headline3 = espn.getHeadline(teamId, 2)
            description1 = espn.getDescription(teamId, 0)
            description2 = espn.getDescription(teamId, 1)
            description3 = espn.getDescription(teamId, 2)
        #team = espn.getName(espn.getTeam(teamId))

        except:
            pass
        return render_template("results.html", 
                               username = username,
                               name=uname1,
                               description = udescription1,
                               movie = movie,
                               #team = team,
                               synopsis = synopsis, 
                               headline1 = headline1,
                               headline2 = headline2,
                               headline3 = headline3,
                               description1 = description1,
                               description2 = description2,
                               description3 = description3,
                               name2 = uname2,
                               udescription2 = udescription2)

if __name__ == "__main__":
    app.run(debug = True)
