from flask import Flask
from flask import session,url_for,request,redirect
from flask import render_template
import mongo

app = Flask(__name__)

quote = wiki-proof.getQuote()
title = wiki-proof.getTitle()

@app.route("/",methods=['GET','POST'])
def Home():

    

if __name__ == "__main__":
    app.debug=True
    app.run()		

