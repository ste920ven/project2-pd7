from flask import Flask, render_template, request, redirect, url_for, session
import db
import api

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    allAlbums = db.getImages()
    if request.method == 'POST':

      #  def avgRatings():
       #     ratings = []
        #    for album in allAlbums:
         #       ratings.append(db.getRating(album))
          #  return ratings
                
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
            
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7202, debug=True)

