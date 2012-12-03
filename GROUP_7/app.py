from flask import Flask, render_template, request, redirect, url_for, jsonify
from api import getAddress, getNearby, isPOI, distanceFrom, durationTo, getNearby

app = Flask(__name__)
global _name

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/get_Address")
def get_Address():
    a = request.args.get('a', 0)
    return jsonify(result=getAddress(a))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=7207)
