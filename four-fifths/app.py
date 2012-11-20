from flask import Flask, render_template, request, redirect, url_for
import extractor
import twilio.twiml

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

@app.route('/twilio')
def twilio():
    resp = twilio.twiml.Response()
    resp.sms("test message!")
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7005, debug=True)
