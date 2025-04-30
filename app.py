
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

    if "buy" in incoming_msg:
        reply = "Great! I can help you with buying a property. Text a number from 1–5 to see available homes."
    elif "sell" in incoming_msg:
        reply = "Awesome! Let's talk about selling your home. I can provide a free evaluation."
    elif "1" in incoming_msg:
        reply = "Property 1: 123 Main St, Warwick RI. 3 bed, 2 bath — $450,000. Want a showing?"
    elif "2" in incoming_msg:
        reply = "Property 2: 456 Oak Dr, Cranston RI. 4 bed, 3 bath — $525,000. Interested?"
    elif "3" in incoming_msg:
        reply = "Property 3: 789 Elm Ln, Providence RI. 2 bed, 2 bath — $390,000. Want more info?"
    elif "4" in incoming_msg:
        reply = "Property 4: 101 Maple Ave, Johnston RI. 3 bed, 2.5 bath — $470,000. Schedule a visit?"
    elif "5" in incoming_msg:
        reply = "Property 5: 202 Pine St, East Greenwich RI. 5 bed, 4 bath — $699,000. Ready to tour?"
    else:
        reply = "Thanks for your message! Type 'buy' or 'sell' to get started."
