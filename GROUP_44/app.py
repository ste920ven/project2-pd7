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
            r1 = request.form.get('zipcode') ##returns "None" - how can i get to return 
                                             ## the text that the user inputs??
            print r1
            return render_template("results.html")


if __name__ == "__main__":
    app.run(debug = True)
