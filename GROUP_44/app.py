from flask import Flask,url_for,redirect,flash,session,escape,request,render_template
from pymongo import connection

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/")
def home():
    return redirect("/survey")

if __name__ == "__main__":
    app.run(debug = True)
