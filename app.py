from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Sample properties
properties = {
    "123 Main St": "123 Main St is a 3 bed, 2 bath house listed at $450,000. Open house this Saturday 12–2 PM.",
    "456 Oak Ave": "456 Oak Ave is a modern condo with 2 beds and 2 baths, priced at $380,000.",
    "789 Pine Rd": "789 Pine Rd is a cozy 4 bed, 3 bath single-family home for $520,000.",
    "101 Elm St": "101 Elm St is a beautiful ranch with 3 beds and 2.5 baths, listed at $470,000.",
    "202 Birch Ln": "202 Birch Ln is a new build with 5 beds and 4 baths, asking price is $650,000."
}

@app.route("/")
def home():
    return "Real Estate Text Bot is Live!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    resp = MessagingResponse()

    response_text = "Sorry, I couldn't find that property. Please ask about: " + ", ".join(properties.keys())
    for address, info in properties.items():
        if address.lower() in msg.lower():
            response_text = info
            break

    resp.message(response_text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
