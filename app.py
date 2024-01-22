import os
from flask import Flask, render_template, request
from moceansdk import Client, Basic
import selfcord
import threading

app = Flask(__name__)
bot = selfcord.Bot()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
TOKEN = os.getenv('TOKEN')

def send_sms(sender_name, recipient_number, message_text):
    if not (API_KEY and API_SECRET):
        return "API key and API secret must be provided"
    mocean = Client(Basic(API_KEY, API_SECRET))
    response = mocean.sms.create({
        "mocean-from": sender_name,
        "mocean-to": recipient_number,
        "mocean-text": message_text,
    }).send()
    return response.get("messages", [{}])[0].get("err_msg")

@bot.on("ready")
async def ready(time):
    print(f"Connected To {bot.user.name}\n Startup took {time:0.2f} seconds")

@bot.on("message")
async def responder(message):
    if message.content.startswith("!send"):
        parts = message.content.split()
        if len(parts) < 4:
            await message.channel.send("Invalid command format. Use: !send <sender> <recipient> <message>")
            return

        err_msg = send_sms(parts[1], parts[2], " ".join(parts[3:]))
        await message.channel.send(err_msg or "Message sent successfully")

@app.route('/', methods=['GET', 'POST'])
def index():
    global API_KEY, API_SECRET
    status_message = None

    if request.method == 'POST':
        API_KEY = request.form.get('api_key') or API_KEY
        API_SECRET = request.form.get('api_secret') or API_SECRET

        err_msg = send_sms(request.form['sender'], request.form['recipient'], request.form['message'])
        status_message = err_msg or "Message sent successfully"

    return render_template('index.html', status_message=status_message, api_key=API_KEY, api_secret=API_SECRET)

def run_bot():
    bot.run(TOKEN)

threading.Thread(target=run_bot).start()

if __name__ == '__main__':
    app.run(debug=False)
