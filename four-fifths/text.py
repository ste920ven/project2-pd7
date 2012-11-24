from flask  import Flask
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

@app.route('/incomingVoice', methods=['GET', 'POST'])
def incomingVoice():
    resp = twiml.Response()
#note: spelled out "fizz" because it probably can't pronounce "phys"
    welcome = "Welcome to the Stuyvesant information hotline. Press one for today's schedule and fizz ed cycle. Press two for the weather at Stuyvesant today."
    resp.say("Welcome to the Stuyvesant information hotline. Press one for today's schedule and fizz ed cycle. Press two for the weather at Stuyvesant today.")
#WARNING: hardcoded url and port
    resp.gather(numDigits=1, action="/schedule")
    return str(resp)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    data = extractor.loadStuySite()
    schedule = extractor.getSchedule(data[1], data[2])
    gymDay = extractor.getGymDay(schedule)
    bellDay = extractor.getBellDay(schedule)
    resp = twiml.Response()
#'a' or 'an' depending on the following word: B1/B2 ('a') or A1/A2/unknown ('an')
    if gymDay[0] == "B" : article = "a"
    else : article = "an"
#remember to account for e.g. "School is closed today"
#instead of "Today's schedule is closed"
    message = "Today's schedule is %s. Today is %s %s day."%(bellDay, article, gymDay) 
    resp.say(message)
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7005, debug=True)
