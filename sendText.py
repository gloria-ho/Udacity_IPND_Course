# Lesson 3.3: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending
# text messages. In this mini-project we'll uses classes
# to send a text message using Twilio, a library we'll
# download from the Internet and add to Python.

from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = " "
# Your Auth Token from twilio.com/console
auth_token  = " "

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+ ", 
    from_="+ ",
    body="Hello from Python!")

print message.sid