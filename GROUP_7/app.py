from flask import Flask, render_template, request, redirect, url_for
import api

app = Flask(__name__)
global _name

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)
