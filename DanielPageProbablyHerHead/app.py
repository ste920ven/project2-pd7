from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

#quote = wiki-proof.getQuote()
#title = wiki-proof.getTitle()

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug=True
    app.run()	

