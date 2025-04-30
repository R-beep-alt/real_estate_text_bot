from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "Real Estate Text Bot is Live!"

@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body").lower()
    resp = MessagingResponse()

    if "buy" in incoming_msg:
        reply = "Great! I can help you with buying a property. Which property are you interested in?"
    elif "sell" in incoming_msg:
        reply = "Awesome! Let's talk about selling your home."
    elif "123 oak st" in incoming_msg:
        reply = "123 Oak St: 3 bed, 2 bath, $450,000. Recently renovated and move-in ready!"
    elif "456 maple ave" in incoming_msg:
        reply = "456 Maple Ave: 4 bed, 3 bath, $525,000. Spacious backyard and quiet neighborhood."
    elif "789 pine ln" in incoming_msg:
        reply = "789 Pine Ln: 2 bed, 1 bath, $350,000. Perfect starter home near downtown."
    elif "321 elm rd" in incoming_msg:
        reply = "321 Elm Rd: 5 bed, 4 bath, $680,000. Luxury living with a private pool."
    elif "654 birch blvd" in incoming_msg:
        reply = "654 Birch Blvd: 3 bed, 2 bath, $480,000. Open house this weekend!"
    else:
        reply = "Thanks for your message! Please type 'buy' or 'sell' or ask about a specific property."

    resp.message(reply)
    return str(resp)
