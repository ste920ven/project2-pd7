from flask import Flask, render_template, request, redirect, url_for
import extractor

app = Flask(__name__)

@app.route('/')
def main():
    news     = extractor.getNews()
    schedule = extractor.getSchedule()
    return render_template('home.html',
                           news=news,
                           schedule=schedule)

if __name__ == '__main__':
    app.debug = True
    app.run()
