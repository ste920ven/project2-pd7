from flask import Flask, render_template, request, redirect, url_for, session
import db

app = Flask(__name__)

#quote = wiki-proof.getQuote()
#title = wiki-proof.getTitle()

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        #allAlbums = db.getImages()
        print str(request.form['button'])
        """
        button = str(request.form['button'])
        if button == "Generate":
            #db.addImage('1')
            print "the generate button was recognized!"
            return render_template("index.html"), 404
        """
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7202, debug=True)
