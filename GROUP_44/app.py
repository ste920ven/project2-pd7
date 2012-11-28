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
        #print "post1"
        if button == 'Save!':
            
            ##GET ZIPCODE
            r1 = request.form.get('zipcode') ##returns Zipcode
            print r1
            ##GET FAV BASEBALL TEAM
            r2 = request.form.get('select1') ##returns fav. baseball team
            print r2
            ######## START CHECKBOXES ###########


     #       r3 = ["test","test2"]
            ##i think i'm going to have to hardcode each checkbox
     #       tmp = request.form['cb1']
     #       if tmp == "on":
     #           r3.append("Action & Adventure")
     #       tmp = request.form['cb2']
     #       if tmp == "on":
     #           r3.append(tmp)
     #       print r3    
            #r3 = request.form['Action']
            #print r3
            #if r3 == "on": ##means it was selected
            #    r3 = Action & Adventure        


            ########### END CHECKBOXES ##############

            ## Interact with APIs ##

            ## End API interaction ##
            return render_template("results.html")


if __name__ == "__main__":
    app.run(debug = True)
