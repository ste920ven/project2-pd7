from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup
import json
import urllib


def test():
    rq = urllib.urlopen("https://api.twilio.com/2010-04-01/Accounts/ACd0dd5dba08dbb56c4c09798da673290d/SMS/Messages.json")
    re = json.loads(rq.read())
    print re;
    recieved=[]
    sent=[]
    for sms in re["sms_messages"]:
        if(sms["status"] == "received"):
            recieved.append(sms["body"])
                            
        if(sms["status"] == "sent"):
            sent.append(sms["body"])
                               
    print "Recieved SMSs:"+ recieved
    print "Sent SMSs:"+ sent
       
    

test()
