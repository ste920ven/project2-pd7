from flask import Flask, render_template, request, redirect, url_for, session
import db
import api
from random import randint

app = Flask(__name__)



@app.route("/",methods=['GET','POST'])
def index():
    allAlbums = db.getImages()
    def randomize():
        randNum = randint(0, 999)
        return allAlbums[randNum]
    if request.method == 'POST':                
        global source
        button = request.form['button']
        if button == 'Generate':
            source = randomize()
            band = api.newArtistName()
            name = api.newAlbumName()
            return render_template("index.html", allAlbums = allAlbums, source = source, band = band, name = name)
    else:
        return render_template("index.html", allAlbums = allAlbums)

            
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9019, debug=True)

