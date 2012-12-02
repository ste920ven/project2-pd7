from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash
import lastfm,database

app=Flask(__name__)
app.secret_key="secret"

#data_artist=api.create_artist()
data_song=lastfm.create_song()
data_album=lastfm.create_album()
username=""
album_name=""
@app.route("/",methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template("home.html")
    if request.method=="POST":
        if (request.form["button"]=="register"):
            username=request.form["name"]
            password=request.form["password"]
            if (database.saveInfo(username,password)):
                flash("Registered successfully!")
            else:
                flash("The name is taken, choose a new name")
            return redirect(url_for("login"))
        if(request.form["button"]=="login"):
            username=request.form["name"]
            password=request.form["password"]
            if (not database.verifyLogin(username,password)):
                flash("Arrh! Wrong password. Try again!")
                return redirect(url_for("login"))
            else:
                return render_template("hello.html",name=username)

@app.route("/hello",methods=['GET','POST'])
def hello():
    if(request.form["button"]=="rate songs"):
        return render_template("song.html", songs=data_song.keys())
    if(request.form["button"]=="rate albums"):
        return render_template("album.html",albums=data_album.keys())

@app.route("/hello/album/<album>",methods=['GET','POST'])
def album(album=""):
    album_name=album
    if(request.method=="GET"):
        tmp=data_album[album]
        return render_template("rate_album.html",album=album,image=tmp["image"],artist=tmp["artist"],rank=tmp["rank"],link=tmp["url"],url=tmp['artist url'])
    if(request.method=="POST"):
        button=request.form["button"]
        if button == "rate":
            rating_value=request.form["rating"]
            comment=request.form["comment"]
            database.addAlbumRatingForUsername(username,album_name,data_album[album_name]["artist"],rating_value,comment)
            return render_template("album.html", albums=data_album.keys())

@app.route("/hello/song/<song>",methods=['GET','POST'])
def song(song=""):
    if(request.method=="GET"):
        return render_template("rate_song.html",song=song,link=data_song[song]["url"],artist=data_song[song]["artist"],image=data_song[song]["image"],rank=data_song[song]["rank"],url=data_song[song]["artist url"])
    if(request.method=="POST"):
        button=request.form["button"]
        if button == "rate":
            rating_value=request.form["rating"]
            comment=request.form["comment"]
            database.addSongRatingForUsername(username,song,data_song[song]["artist"],rating_value,comment)
            return render_template("song.html", songs=data_song.keys())
'''
@app.route("/hello/artist/<artist>",methods=['GET','POST'])
def artist(artist=""):
    if(request.method=="GET"):
        return render_template("rate_artist.html",artist=artist,link=data_artist[artist]["url"])
    if(request.method=="POST"):
        button=request.form["button"]
        if button == "rate":
            #need to be stored in a database
            rating_value=request.form["rating"]
            #need to be stored in a database
            comment=request.form["comment"]
            return render_template("artist.html", artists=data_artist.keys())
'''
if __name__=="__main__":
    app.debug=True
    app.run(port=5000)
