from twilio.rest import TwilioRestClient
import json
import urllib

def getRecords(user):
    records = json.loads(urllib.urlopen("https://api.twilio.com/2010-04-01/Accounts/ACd0dd5dba08dbb56c4c09798da673290d/SMS/Messages.json").read())
    received = []
    for sms in records["sms_messages"]:
        if(sms["status"] == "received"):
            recieved.append(sms["body"]) 
    return received
