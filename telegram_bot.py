import os
from dotenv import load_dotenv

from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext

load_dotenv()

token = os.getenv("bot_token")
updater = Updater(token, use_context=True)
updater.start_polling()
dispatcher = updater.dispatcher 

def send_text(chat_id, text:str):
    updater.bot.send_message(chat_id, text)

def send_image(chat_id, image):
    with open(image, "rb") as photo:
        updater.bot.send_photo(chat_id, photo)

def stop():
    updater.stop()