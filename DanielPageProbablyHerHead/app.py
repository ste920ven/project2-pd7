from flask import Flask, render_template, request, redirect, url_for, session
import db

app = Flask(__name__)

#quote = wiki-proof.getQuote()
#title = wiki-proof.getTitle()

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        allAlbums = db.getImages()
        if request.form['button'] == 'Generate stuff!':
            db.addImage('1')
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)	
    app.run()
