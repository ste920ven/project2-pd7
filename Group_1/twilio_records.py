from twilio.rest import TwilioRestClient
import json
import urllib

account = 'ACf662305afa76bba6f077405676222615'
token = '73452f5f4a6931a17ce11c93d6b6b473'
client = TwilioRestClient(account,token)

def get_records(number):
    messages = client.sms.messages.list()
    sent={}
    for sms in messages:
        if str(sms.status)=="sent" and int(sms.to) == int(number):
            key = sms.body[6:sms.body.find('\n')]
            sent[key]=sms.body                               
    return sent
