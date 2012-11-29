from flask import Flask,url_for,redirect,flash,session,escape,request,render_template
from pymongo import connection
import upcoming
#import espn
#import factual

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        print "get!!"
        return render_template("survey.html")
    else:
        button=request.form.get('button',"")
        #print "post1"
        if button == 'Save!':            
            ##GET ZIPCODE
            r1 = request.form['zipcode'] ##returns Zipcode
            print r1
            ##GET FAV BASEBALL TEAM
            r2 = request.form['select1'] ##returns fav. baseball team
            print r2
            ##Get Genre
            r3 = request.form['Genres']
            print r3
            ##Get Cuisine
            r4 = request.form['Cuisines']
            print r4

            #### Interact with APIs ####
    ##remember to hard code in s/t nothing can  be left blank 
            s3 = upcoming.getEvent(r3,r1)
            print s3

            #### End API interaction ####

            return render_template("results.html")


if __name__ == "__main__":
    app.run(debug = True)
