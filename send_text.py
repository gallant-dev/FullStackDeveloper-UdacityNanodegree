from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC584e41832bf402fb68e42a340c7eeafe"
# Your Auth Token from twilio.com/console
auth_token  = "3f4dfa8bd15c8d3fb3157448ed445529"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+19055374937", 
    from_="+12897688709",
    body="I'm Thor!")

print(message.sid)
