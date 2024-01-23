import os
from flask import Flask, render_template, request
from moceansdk import Client, Basic
import selfcord
import threading
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, filters, Updater, CallbackContext

app = Flask(__name__)
discord_bot = selfcord.Bot()
telegram_bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
updater = Updater(bot=telegram_bot, use_context=True)

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

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

def telegram_command_handler(update: Update, context: CallbackContext):  # Updated method signature
    message = update.message.text.split()
    if len(message) < 4:
        update.message.reply_text("Invalid command format. Use: /send <sender> <recipient> <message>")
        return

    err_msg = send_sms(message[1], message[2], " ".join(message[3:]))
    update.message.reply_text(err_msg or "Message sent successfully")

def start_command_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello! 👋 I'm your SMS bot. Here's how to use me:\n"
        "/send <sender> <recipient> <message>\n\n"
        "<sender> - Your name or identifier.\n"
        "<recipient> - Recipient's phone number.\n"
        "<message> - Message to send.\n\n"
        "Example:\n/send John +1234567890 Hello, this is a test."
    )

updater.dispatcher.add_handler(CommandHandler('start', start_command_handler))
updater.dispatcher.add_handler(CommandHandler('send', telegram_command_handler))

@discord_bot.on("ready")
async def ready(time):
    print(f"Connected To {discord_bot.user.name}\n Startup took {time:0.2f} seconds")

@discord_bot.on("message")
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

def run_discord_bot():
    discord_bot.run(DISCORD_TOKEN)

def run_telegram_bot():
    updater.start_polling()

threading.Thread(target=run_discord_bot).start()
threading.Thread(target=run_telegram_bot).start()

if __name__ == '__main__':
    app.run(debug=False)
