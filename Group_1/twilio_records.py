from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup
import json
import urllib


def get_records(number):
    rq = urllib.urlopen("https://api.twilio.com/2010-04-01/Accounts/ACf662305afa76bba6f077405676222615/SMS/Messages.json")
    re = json.loads(rq.read())
    sent={}
    for sms in re["sms_messages"]:
        if sms["status"] == "sent" and sms["to"] == number:
            key = sms['body'][6:sms['body'].find('\n')]
            sent[key]=sms['body']                               
    return sent

    
