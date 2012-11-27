from flask import Flask, request, redirect
import twilio.twiml
import factual_search

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    text = request.values.get('Body', None)
    result = factual_search.getSearchString(text)
    resp = twilio.twiml.Response()
    resp.sms(result)
    #resp.sms("Hello")
    return str(resp)
 
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=7001, debug=True)
