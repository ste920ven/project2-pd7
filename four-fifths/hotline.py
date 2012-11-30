from flask  import Flask, request, url_for
from twilio import twiml
import extractor, Weather
import random

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
    audio = []
    audio.append("welcome-1.mp3")
    audio.append("press-1.mp3")
    audio.append("press-2.mp3")
#don't have MTA page just yet
#audio.append("press-3.mp3")
    audio.append("press-4.mp3")
    gather = resp.gather(numDigits=1, action="/choice")
    for each in audio:
        url = url_for("static", filename=("audio/%s"%(each)))
        gather.play(url)
    return str(resp)

@app.route('/choice', methods=['POST'])
def schedule():
    digit = request.form['Digits']
    resp = twiml.Response()
    audio = []

#---pressed 1: schedule---
    if int(digit) == 1 :
        print "1 case: schedule"
        data = extractor.loadStuySite()
        schedule = extractor.getSchedule(data[1], data[2])
        bellDay = extractor.getBellDay(schedule)
        #sentence for schedule type, plus phys. ed. cycle if applicable
        if bellDay == "Closed" :
            audio.append("Closed.mp3")
        elif bellDay == "Weekend" :
            audio.append("Closed.mp3")
        elif bellDay == "Unknown" :
            audio.append("Unknown.mp3")
        else :
            gymDay = extractor.getGymDay(schedule)
            #depends on mp3s with same names as bellDay, gymDay  options
            audio.append("%s.mp3"%(bellDay))
            audio.append("cycle.mp3")
            audio.append("%s.mp3"%(gymDay))   
         
#---pressed 2: weather---
    elif int(digit) == 2 :
        print "2 case: weather"
        temp = Weather.getTemp()
        high = Weather.getHigh()
        low = Weather.getLow()
        #"Today the high will be __ Fahrenheit."
        audio.append("high.mp3")
        #one of the number mp3s
        if high < 0 :
            audio.append("negative.mp3")
        audio.append("%d.mp3"%(abs(high)))
#NOTE: TRIM 'OR' FROM 'FAHRENHEIT, OR'
#!!!!!!!!!
        audio.append("fahrenheit.mp3")
        #"and the low will be __ Fahrenheit."
        audio.append("low.mp3")
        if low < 0 :
            audio.append("negative.mp3")
        audio.append("%d.mp3"%(low))
        audio.append("fahrenheit.mp3")
        #"It is now __ Fahrenheit"
        audio.append("now.mp3")
        if now < 0 :
            audio.append("negative.mp3")
        audio.append("%d.mp3"%(temp))
        audio.append("fahrenheit.mp3")

#---pressed 4: credits---
    elif int(digit) == 4 :
        audio.append("credits.mp3")

#---pressed another button---
    else :
        print "Not valid number. Bad user."
        #"You pressed some other number. Bad user."
        audio.append("baduser.mp3")

    #"Press any button to go back."
    audio.append("back.mp3")
    #play all queued audio, accepting any button as an interrupt
    gather = resp.gather(numDigits=1, action="/chance", timeout=10)
    for each in audio:
        url = url_for("static", filename=("audio/%s"%(each)))
        gather.play(url)
    return str(resp)

@app.route("/chance", methods = ['POST'])
def chance():
#user has two seconds to press any button and get an easter egg
    resp = twiml.Response()
    resp.gather(numDigits=1, action = '/egg', timeout = 2)
    resp.redirect(url="/incomingVoice")
    return str(resp)

@app.route("/egg", methods = ['POST'])
#play one of the fourteen easter eggs at random
def egg():
    resp = twiml.Response()
    url = url_for("static", filename=("audio/egg-%d.mp3"%(random.randint(1,13))))
    resp.play(url)
    resp.redirect(url="/incomingVoice")
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7255)
