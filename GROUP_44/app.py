from flask import Flask,url_for,redirect,flash,session,escape,request,render_template
from pymongo import connection

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        print "get!!"
        return render_template("survey.html")
    else:
        button=request.form.get('button',"")
        print "post1"
        if button == 'Save!':
            print "post works!!"
            r1 = request.form.get('zipcode') ##returns Zipcode
            #print r1
            r2 = request.form.get('select1') ##returns fav. baseball team
            #print r2
            r3 = request.form['Action']
            print r3
            if r3 == "on":
                ##means it was selected
                return Action
            return render_template("results.html")


if __name__ == "__main__":
    app.run(debug = True)
