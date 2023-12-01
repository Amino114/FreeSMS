from flask import Flask, render_template, request
from moceansdk import Client, Basic

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global API_KEY, API_SECRET
    status_message = None

    if request.method == 'POST':
        sender_name = request.form['sender']
        recipient_number = request.form['recipient']
        message_text = request.form['message']

        # Check if API_KEY and API_SECRET have been submitted
        if 'api_key' in request.form and request.form['api_key']:
            API_KEY = request.form['api_key']
        else:
            API_KEY = '81574658'
        if 'api_secret' in request.form and request.form['api_secret']:
            API_SECRET = request.form['api_secret']
        else:
            API_SECRET = '6f4558e2'

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

    # Set api_key and api_secret to hardcoded values if not submitted
    api_key = API_KEY if 'api_key' in request.form and request.form['api_key'] else ''
    api_secret = API_SECRET if 'api_secret' in request.form and request.form['api_secret'] else ''

    return render_template('index.html', status_message=status_message, api_key=api_key, api_secret=api_secret)

if __name__ == '__main__':
    app.run(debug=True)
