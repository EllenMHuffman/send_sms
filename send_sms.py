import os
from twilio.rest import Client

ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
MY_PHONE = os.environ['MY_PHONE']
TWILIO_PHONE = os.environ['TWILIO_PHONE']

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    to=MY_PHONE,
    from_=TWILIO_PHONE,
    body="Testinggggggg")

print(message.sid)
