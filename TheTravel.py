import os, sys
from flask import Flask, request
import json
from pymessenger import Bot
from pprint import pprint
from utils import generate_user_response
from utils import get_wit_response

VERIFICATION_TOKEN = "hello"
ACCES_VERIFECATION_TOKEN="EAAHXInhE5AsBAHxpGZAt0sSlI0Mj5ukjL1AJ5LUCFlEwN5p6WxZASdv096nR0iF0RPyzJum5iu4gPA9r8bjSSL4aLsvXiPzTa8XZBoobURPKoDE8gvFqyYl0GSjPUERhE6b5rwaokAOKTrFmVhajThwMJNcdEfBpuIRcsGKWM2TEZALI0gwpEcI6NIONUZBgrPzLOxlF0XQZDZD"

app = Flask(__name__)
bot = Bot(ACCES_VERIFECATION_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN: #you can replace VERIFICATION_TOKEN with os.environ["VERIFY_TOKEN"]
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello-world", 200

@app.route('/', methods=['POST'])
def webhook():
        printmsg("Starting Webhook")
        data = request.get_json()
        process_data(data)
        return "okk",200

def process_data(data):
    #Check if value correponding to object key is "page"
    if data["object"]=="page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                sender_id = messaging_event["sender"]["id"]
                recipient_id = messaging_event["recipient"]["id"]
                if messaging_event.get("message"):
                    if "text" in messaging_event["message"]:#there is text key
                        messaging_text = messaging_event["message"]["text"]
                    else:
                        messaging_text = "no text"
                    response = generate_user_response(messaging_text)
                    bot.send_text_message(sender_id,response)


def printmsg(msg):
        print(msg)
        sys.stdout.flush()

if __name__=="__main__":
    app.run(debug=True, port=80)
