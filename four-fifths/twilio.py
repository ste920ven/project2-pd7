from flask import Flask
import extractor
from twilio import twiml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def twilio():
    resp = twiml.Response()
    message = "test message"
    resp.sms(message)
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=7005, debug=True)
