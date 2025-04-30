
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "Real Estate Text Bot is Live!"

@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body")
    resp = MessagingResponse()
    reply = "Thanks for your message!"

    if "buy" in incoming_msg.lower():
        reply = "Great! I can help you with buying a property."
    elif "sell" in incoming_msg.lower():
        reply = "Awesome! Let's talk about selling your home."

    resp.message(reply)
    return str(resp)
