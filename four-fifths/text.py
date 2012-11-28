from flask  import Flask, request, url_for
from twilio import twiml
import extractor

app = Flask(__name__)

@app.route('/text', methods=['GET', 'POST'])
def text():
    data = extractor.loadStuySite()
    schedule = extractor.getSchedule(data[1], data[2])
    bellDay = extractor.getBellDay(schedule)
    resp = twiml.Response()
    if bellDay == "Closed" :
        message = "School is closed today."
    elif bellDay == "Weekend" :
        message = "It's a weekend. There is no school today."
    elif bellDay == "Unknown" :
        message = "We don't have today's schedule. How embarrassing."
    else :
#'a' or 'an' depending on the next word:
#B1/B2 ('a') or A1/A2/Unknown ('an')
        gymDay = extractor.getGymDay(schedule)
        if gymDay[0] == "B" : article = "a"
        else : article = "an"
        message = "Today is a %s schedule. Today is %s %s day."%(bellDay, article, gymDay)
    resp.sms(message)
    return str(resp)

@app.route('/incomingVoice', methods=['POST'])
def incomingVoice():
    resp = twiml.Response()
#note: spelled out "fizz" because it probably can't pronounce "phys"
#    welcome = "Welcome to the Stuyvesant information hotline. Press one for today's schedule and fizz ed cycle. Press two for the weather at Stuyvesant today."
 #   resp.gather(numDigits=1, action="/scheduleweather").say(welcome)
    audio = []
    audio.append("A.mp3")
    audio.append("A1.mp3")
    audio.append("A2.mp3")
#don't have MTA or info pages just yet
#  audio.append("press-3.mp3")
#  audio.append("press-4.mp3")
    for each in audio:
        url = url_for("static", filename=("audio/%s"%(each)))
        resp.gather(numDigits=1, action="/scheduleweather").play(url)
    return str(resp)

@app.route('/scheduleweather', methods=['POST'])
def schedule():
    digit = request.form['Digits']
    resp = twiml.Response()
#---pressed 1: schedule---
    if int(digit) == 1 :
        print "1 case: schedule"
        data = extractor.loadStuySite()
        schedule = extractor.getSchedule(data[1], data[2])
        bellDay = extractor.getBellDay(schedule)
        if bellDay == "Closed" :
            message = "School is closed today."
        elif bellDay == "Weekend" :
            message = "It's a weekend. There is no school today."
        elif bellDay == "Unknown" :
            message = "We don't have today's schedule. How embarrassing."
        else :
#'a' or 'an' depending on the next word:
#B1/B2 ('a') or A1/A2/Unknown ('an')
            gymDay = extractor.getGymDay(schedule)
            if gymDay[0] == "B" : article = "a"
            else : article = "an"
            message = "Today is a %s schedule. Today is %s %s day."%(bellDay, article, gymDay)
#---pressed 2: weather---
    elif int(digit) == 2 :
        print "2 case: weather"
        message = "We don't have a working weather system yet. Our apologies."
#---pressed another button
    else :
        print "Not 1 or 2. Bad user."
        message = "You didn't press one or two. Bad user."
    message += " Press any key to go back."
    resp.gather(numDigits=1, action="/incomingVoice").say(message)
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7255, debug=True)
