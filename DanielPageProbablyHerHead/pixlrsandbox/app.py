from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/save/", methods=['GET', 'POST'])
def save():
    if request.method == 'GET':
        print request.args
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=9018, debug=True)
