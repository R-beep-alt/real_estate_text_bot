from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# === PROPERTY DATABASE ===
properties = {
    "12 taylor drive rehoboth ma": {
        "price": "$689,000",
        "bedrooms": 4,
        "bathrooms": 3,
        "sqft": "3,200"
    }
}

# === HANDLING INCOMING TEXTS ===
@app.route("/sms", methods=['POST'])
def sms_reply():
    incoming_msg = request.form.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    found = False
    for address, details in properties.items():
        if address in incoming_msg:
            reply = (f"Property at {address}:\n"
                     f"Price: {details['price']}\n"
                     f"Bedrooms: {details['bedrooms']}\n"
                     f"Bathrooms: {details['bathrooms']}\n"
                     f"Square Feet: {details['sqft']}")
            msg.body(reply)
            found = True
            break

    if not found:
        msg.body("Sorry, I couldn't find that property. Can you double-check the address?")

    return str(resp)

if __name__ == "__main__":
    app.run()
