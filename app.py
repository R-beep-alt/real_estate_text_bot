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

    # Property responses
    if "123 main" in incoming_msg:
        reply = "123 Main St is a 3-bed, 2-bath home listed at $450,000. Would you like more info?"
    elif "19 pine" in incoming_msg:
        reply = "19 Pine Ct is a quiet cul-de-sac home, 3-bed, 2 bath with a big backyard."
    elif "5 broad" in incoming_msg:
        reply = "5 Broadway Ave is a modern condo with 2 bedrooms, priced at $375,000."
    elif "42 oak" in incoming_msg:
        reply = "42 Oak Dr is a cozy 1-bed, 1-bath starter home, listed at $250,000."
    elif "77 beach" in incoming_msg:
        reply = "77 Beach Rd is a waterfront 4-bed, 3-bath beauty for $950,000."

    # General replies
    elif "buy" in incoming_msg:
        reply = "Great! I can help you with buying a property."
    elif "sell" in incoming_msg:
        reply = "Awesome! Let's talk about selling your home."
    else:
        reply = "Thanks for your message! Text the address or say 'buy' or 'sell'."

    resp.message(reply)
    return str(resp)
