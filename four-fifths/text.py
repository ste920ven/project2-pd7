from flask  import Flask
from twilio import twiml
import extractor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def twilio():
    schedule = extractor.getSchedule()
    resp = twiml.Response()
    ab = extractor.getGymDay(schedule)
    bell = extractor.getBellDay(schedule)
    message = "Today's Phys. Ed. cycle is %s. Today's schedule is %s."%(ab, bell)
    resp.sms(message)
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7005, debug=True)
