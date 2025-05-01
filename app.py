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

    # Default reply
    reply = "Thanks for your message!"

    # Property logic
    if "buy" in incoming_msg:
        reply = "Great! I can help you with buying a property."
    elif "sell" in incoming_msg:
        reply = "Awesome! Let's talk about selling your home."
    elif "123 pine st" in incoming_msg:
        reply = "123 Pine St is a 3-bed, 2-bath home listed at $420,000. Want a showing?"
    elif "45 oak ave" in incoming_msg:
        reply = "45 Oak Ave is a 4-bed, 3-bath modern home for $560,000. Interested?"
    elif "77 river rd" in incoming_msg:
        reply = "77 River Rd is a waterfront 2-bed for $395,000. Want more info?"
    elif "22 elm dr" in incoming_msg:
        reply = "22 Elm Dr is a ranch with 5 acres at $610,000. Need a virtual tour?"
    elif "99 maple ln" in incoming_msg:
        reply = "99 Maple Ln is a fixer-upper listed at $250,000. Want to walk through it?"

    resp.message(reply)
    return str(resp)#
