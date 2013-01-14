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
images_song=lastfm.create_song_images()
images_album=lastfm.create_album_images()
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
                return redirect(url_for("hello"))

@app.route("/hello",methods=['GET','POST'])
def hello():
    if request.method == "GET":
        return render_template("hello.html",name=username)
    if request.method == "POST":    
        if(request.form["button"]=="rate songs"):
             return render_template("song.html", songs=data_song.keys())
        if(request.form["button"]=="rate albums"):
             return render_template("album.html",albums=data_album.keys())

@app.route("/hello/album/<album>",methods=['GET','POST'])
def album(album=""):
    if(request.method=="GET"):
        tmp=data_album[album]
        try:
            ratings=database.getAlbumRating(album,tmp["artist"])
            average=database.getAverageRating(album,tmp["artist"])
        except Exception:
            ratings=False
            average="No ratings yet, rate this album now!"
        return render_template("rate_album.html",albums=data_album.keys(),album=album,image=tmp["image"],artist=tmp["artist"],rank=tmp["rank"],link=tmp["url"],url=tmp['artist url'],ratings=ratings,average=average)
    if(request.method=="POST"):
        button=request.form['button']
        if button == 'rate':
            rating_value=request.form['rating']
            comment=request.form['comment']
            name=request.form['albumname']
            database.addAlbumrating(username,name,data_album[name]["artist"],rating_value,comment)
            return render_template("album.html", albums=data_album.keys())
        elif button == 'back':
            return redirect(url_for('hello'))

@app.route("/hello/song/<song>",methods=['GET','POST'])
def song(song=""):
    if(request.method=="GET"):
        try:
            ratings=database.getSongRating(song,data_song[song]["artist"])
            average=database.getAverageSongRating(song,data_song[song]["artist"])
        except Exception:
            ratings=False;
            average="No ratings yet, rate this song now!";
        return render_template("rate_song.html",songs=data_song.keys(),song=song,link=data_song[song]["url"],artist=data_song[song]["artist"],image=data_song[song]["image"],rank=data_song[song]["rank"],url=data_song[song]["artist url"],average=average,ratings=ratings)
    if(request.method=="POST"):
        button=request.form["button"]
        if button == "rate":
            rating_value=request.form["rating"]
            comment=request.form["comment"]
            name=request.form["songname"]
            database.addSongRating(username,name,data_song[name]["artist"],rating_value,comment)
            return render_template("song.html", songs=data_song.keys())
        elif button == 'back':
            return redirect(url_for('hello'))

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=7200)
