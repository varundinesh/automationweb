#python code to send messages to the phone using twilio API
from twilio.rest import Client
# Your Account SID from twilio.com/console
#expired tokens
account_sid = "ACb85230b120e3acadebe893cf0bd56e6c"
# Your Auth Token from twilio.com/console
auth_token  = "628041d6ba8ced55fbf5c350b1f3888a"
x=40
client = Client(account_sid, auth_token)
#creating the message structure.
message = client.messages.create(
    to="+91 9496308948",
    from_="+1 774-567-7189 ",
    body="%d "%x)

print(message.sid)
