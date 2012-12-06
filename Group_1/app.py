from flask import Flask, request, redirect, render_template, session,url_for,flash
import twilio.twiml
import factual_search
import urllib2
import math
import twilio_records

app = Flask(__name__)
 

@app.route("/", methods=['GET', 'POST'])
def sendSMS():
    text = request.values.get('Body', None)
    result = factual_search.getSearchString(text)
    resp = twilio.twiml.Response()
    resp.sms(result)
    #resp.sms("Hello")
    return str(resp)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7251, debug=False)
