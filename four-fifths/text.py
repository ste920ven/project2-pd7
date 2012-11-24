from flask  import Flask, request
from twilio import twiml
import extractor

app = Flask(__name__)

@app.route('/text', methods=['GET', 'POST'])
def text():
    data = extractor.loadStuySite()
    schedule = extractor.getSchedule(data[1], data[2])
    resp = twiml.Response()
    gymDay = extractor.getGymDay(schedule)
    bellDay = extractor.getBellDay(schedule)
    message = "Today's Phys. Ed. cycle is %s. Today's schedule is %s."%(gymDay, bellDay)
    resp.sms(message)
    return str(resp)

@app.route('/incomingVoice', methods=['POST'])
def incomingVoice():
    resp = twiml.Response()
#note: spelled out "fizz" because it probably can't pronounce "phys"
    welcome = "Welcome to the Stuyvesant information hotline. Press one for today's schedule and fizz ed cycle. Press two for the weather at Stuyvesant today."
    resp.say(welcome)
    resp.gather(numDigits=1, action="/scheduleweather")
    return str(resp)
#self.request.get('Digits')
@app.route('/scheduleweather', methods=['POST'])
def schedule():
    digit = request.form['Digits']
    print digit
    resp = twiml.Response()
    if str(digit) == '1' :
        data = extractor.loadStuySite()
        schedule = extractor.getSchedule(data[1], data[2])
        gymDay = extractor.getGymDay(schedule)
        bellDay = extractor.getBellDay(schedule)
#'a' or 'an' depending on the next word: B1/B2 ('a') or A1/A2/unknown ('an')
        if gymDay[0] == "B" : article = "a"
        else : article = "an"
#remember to account for e.g. "School is closed today"
#instead of "Today's schedule is closed"
        message = "Today's schedule is %s. Today is %s %s day."%(bellDay, article, gymDay)
    if str(digit) == '2' :
        message = "We don't have a working weather system yet, but we can tell that you pressed two!"
    else : message = "You didn't press one or two. Bad user."
    resp.say(message)
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7005, debug=True)
