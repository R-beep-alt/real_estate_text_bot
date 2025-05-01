
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

    if incoming_msg:
        msg_lower = incoming_msg.lower()
        if "buy" in msg_lower:
            reply = "Great! I can help you with buying a property."
        elif "sell" in msg_lower:
            reply = "Awesome! Let's talk about selling your home."
        elif "123 main" in msg_lower:
            reply = "123 Main St: 3 bed, 2 bath, $450k. Want to schedule a tour?"
        elif "456 oak" in msg_lower:
            reply = "456 Oak Ave: 4 bed, 3 bath, $550k. Great schools nearby!"
        elif "789 pine" in msg_lower:
            reply = "789 Pine Rd: 2 bed, 1 bath, $350k. Cozy and affordable!"
        elif "321 maple" in msg_lower:
            reply = "321 Maple Dr: 5 bed, 4 bath, $750k. Recently renovated!"
        elif "654 elm" in msg_lower:
            reply = "654 Elm St: 3 bed, 2.5 bath, $480k. Nice backyard!"
        else:
            reply = "Thanks for your message! Text 'buy' or 'sell' to get started."
    else:
        reply = "Empty message received."

    resp.message(reply)
    return str(resp)
