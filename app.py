from flask import Flask, request
from flask_cors import CORS
from ProcessData.main import ProcessData

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to my application"


@app.route("/api/sms/", methods=['GET', 'POST'])
def receive_sms_data():
    if request.method == "POST":
        contents = request.get_json()
        messages_array = contents['messages']
        Response = ProcessData.messages(messageArray=messages_array)
        # alert the use or the respective authority
