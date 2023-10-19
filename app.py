from flask import Flask, render_template, request, redirect, url_for
import time
from moceansdk import Client, Basic

app = Flask(__name__)

# Define your Mocean API credentials (replace with secure storage)
API_KEY = "0f90cc72"
API_SECRET = "1db2dd9b"

@app.route('/', methods=['GET', 'POST'])
def index():
    status_message = None

    if request.method == 'POST':
        sender_name = request.form['sender']
        recipient_number = request.form['recipient']
        message_text = request.form['message']

        mocean = Client(Basic(API_KEY, API_SECRET))

        try:
            response = mocean.sms.create({
                "mocean-from": sender_name,
                "mocean-to": recipient_number,
                "mocean-text": message_text,
            }).send()
            print(response)

            # Extract the status code and err_msg from the response
            status_code = response.get("messages", [{}])[0].get("status", -1)
            err_msg = response.get("messages", [{}])[0].get("err_msg")

            # Check for successful response (no err_msg)
            if not err_msg:
                status_message = "Message sent successfully"
            else:
                status_message = err_msg or "Unknown error occurred"

        except Exception as e:
            status_message = f"An error occurred: {e}"

    return render_template('index.html', status_message=status_message)

if __name__ == '__main__':
    app.run(debug=True)
