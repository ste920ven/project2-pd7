from flask  import Flask
from twilio import twiml
import extractor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def twilio():
    resp = twiml.Response()
    ab = extractor.getGymDay()
    bell = extractor.getBellDay()
    message = "Today's Phys. Ed. cycle is %s. Today's schedule is %s."%(ab, bell)
    resp.sms(message)
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7005, debug=True)
