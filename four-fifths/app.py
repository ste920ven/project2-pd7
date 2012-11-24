from flask import Flask, render_template, request, redirect, url_for
import extractor

app = Flask(__name__)

@app.route('/')
def main():
    data     = extractor.loadStuySite()
    news     = extractor.getNews(data[0])
    schedule = extractor.getSchedule(data[1],data[2])
    bellDay  = extractor.getBellDay(schedule)
    gymDay   = extractor.getGymDay(schedule)
    date     = extractor.getDate()
    return render_template('home.html',
                           news=news,
                           schedule=schedule,
                           bellDay=bellDay,
                           gymDay=gymDay,
                           date=date)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, debug=True)
