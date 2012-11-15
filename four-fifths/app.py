from flask import Flask, render_template, request, redirect, url_for
import extractor

app = Flask(__name__)

@app.route('/')
def main():
    news     = extractor.getNews()
    schedule = extractor.getSchedule()
    bellDay  = extractor.getBellDay(schedule)
    date     = extractor.getDate()
    return render_template('home.html',
                           news=news,
                           schedule=schedule,
                           bellDay=bellDay,
                           date=date)

if __name__ == '__main__':
    app.debug = True
    app.run()
