from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "Real Estate Text Bot is Live!"

@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body", "").lower()
    resp = MessagingResponse()

    reply = "Thanks for your message!"

    if "buy" in incoming_msg:
        reply = "Great! I can help you with buying a property."
    elif "sell" in incoming_msg:
        reply = "Awesome! Let's talk about selling your home."
    elif "123 main st" in incoming_msg:
        reply = "123 Main St is a 3-bed, 2-bath home listed at $450,000. Would you like a tour?"
    elif "456 oak ave" in incoming_msg:
        reply = "456 Oak Ave is a cozy 2-bed, 1-bath condo for $299,000. Want more details?"
    elif "789 elm rd" in incoming_msg:
        reply = "789 Elm Rd is a luxury 4-bed, 3-bath with a pool listed at $750,000."
    elif "22 beach blvd" in incoming_msg:
        reply = "22 Beach Blvd is oceanfront, 2-bed, 2-bath at $675,000. Schedule a visit?"
    elif "19 pine ct" in incoming_msg:
        reply = "19 Pine Ct is a quiet cul-de-sac home, 3-bed, 2-bath for $410,000."

    resp.message(reply)
    return str(resp)
