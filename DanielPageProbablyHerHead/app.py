from flask import Flask, render_template, request, redirect, url_for, session
import db

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    #allAlbums = db.getImages()
    if request.method == 'POST':
        print str(request.form['button'])
        """
        button = str(request.form['button'])
        if button == "Generate":
            #db.addImage('1')
            print "the generate button was recognized!"
            return render_template("index.html"), 404
        """
        """
        if request.form['button'] == 'Save':
            db.addImage("http://farm9.staticflickr.com/8070/8234964776_708125d9a6_z.jpg")
        """
    else:
        #return render_template("index.html", allAlbums = allAlbums)
        return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7202, debug=True)
