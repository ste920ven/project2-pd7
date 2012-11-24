from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash
import api

app=Flask(__name__)

data_artist=api.create_artist()
data_song=api.create_song()
data_album=api.create_album()

@app.route("/",methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template("home.html")
    if request.method=="POST":
        if (request.form["button"]=="login"):
            return render_template("hello.html",name=request.form["name"])

@app.route("/hello",methods=['GET','POST'])
def hello():
    if(request.form["button"]=="rate artists"):
        return render_template("artist.html", artists=data_artist.keys())

@app.route("/hello/artist/<artist>",methods=['GET','POST'])
def artist(artist=""):
    return render_template("rate_artist.html",artist=artist)
    




if __name__=="__main__":
    app.debug=True
    app.run(port=5000)
