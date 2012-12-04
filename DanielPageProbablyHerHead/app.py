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
            return render_template("index.html", allAlbums = allAlbums, source = source, band = band, name = name)
        if button == 'Save':
            db.addImage(source)
            return render_template("index.html", allAlbums = allAlbums, source = source)
        if button == 'Edit':
            return render_template("index.html", allAlbums = allAlbums)
    else:
        return render_template("index.html", allAlbums = allAlbums)

@app.route("/<rating>")
def applyrating(rating):
    return render_template('index.html', rating = rating)
            
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7202, debug=True)

