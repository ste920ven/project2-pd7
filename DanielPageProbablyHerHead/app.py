from flask import Flask, render_template, request, redirect, url_for, session
import db

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    allAlbums = db.getImages()
    if request.method == 'POST':
        button = request.form['button']
        if button == 'Save':
            db.addImage("http://farm9.staticflickr.com/8070/8234964776_708125d9a6_z.jpg")
            return render_template("index.html", allAlbums = allAlbums)
        if button == 'Edit':
            return render_template("index.html", allAlbums = allAlbums)
        if button == 'Generate':
            source = "http://farm9.staticflickr.com/8070/8234964776_708125d9a6_z.jpg"
            return render_template("index.html", allAlbums = allAlbums, source = source)
    else:
        return render_template("index.html", allAlbums = allAlbums)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7202, debug=True)
