#python programme to make call to a mobile phone using twilio API
from twilio.rest import Client

# Get these credentials from http://twilio.com/user/account
#these are expired tokens
account_sid = "ACb85230b120e3acadebe893cf0bd56e6c"
auth_token = "628041d6ba8ced55fbf5c350b1f3888a"
client = Client(account_sid, auth_token)

# Make the call
call = client.api.account.calls\
      .create(to="+91 9496308948",  # Any phone number
              from_="+1 774-567-7189 ", # Must be a valid Twilio number
              url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

print(call.sid)
