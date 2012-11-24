from twilio.rest import TwilioRestClient

ACCOUNT_SID = "ACd0dd5dba08dbb56c4c09798da673290d"
AUTH_TOKEN = "cede4a5fd7062c2ccf1f7654b7bdb9fe"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.sms.messages.create(to="16466332978",
                                     from_="+16464624622",
                                     body="Hello!")
