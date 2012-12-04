from flask import Flask, render_template, request, redirect, url_for, session
import db
import api
import xml

app = Flask(__name__)



@app.route("/",methods=['GET','POST'])
def index():
    allAlbums = db.getImages()
    if request.method == 'POST':                
        global source
        button = request.form['button']
        if button == 'Generate':
            source = api.newAlbumPicture()
            band = api.newArtistName()
            name = api.newAlbumName()
            return render_template("index1.html", allAlbums = allAlbums, source = source, band = band, name = name)
    else:
        return render_template("index1.html", allAlbums = allAlbums)

            
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7202, debug=True)

