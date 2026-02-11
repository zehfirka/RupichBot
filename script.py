import os
import logging
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

# Токен з Render Environment Variables!
TOKEN = os.getenv('TOKEN')
if not TOKEN:
    print("ПОМИЛКА: Додай TOKEN в Render Environment Variables!")
    exit(1)

TRANSLIT_MAP = {
    'р': 'r', 'у': 'u', 'п': 'p', 'і': 'i', 'ч': 'ch',
    'з': 'z', 'я': 'ya', 'н': 'n', 'а': 'a',
    'ф': 'f', 'н': 'n', 'у': 'u', 'к': 'k'
}

def normalize(text):
    norm = text.lower()
    for cyr, lat in TRANSLIT_MAP.items():
        norm = norm.replace(cyr, lat)
    return norm

RESPONSES = {
    'rupich': 'РУПІЧ ЧМО!',
    'rupiziana': 'РУПІЧ ЧМО!',
    'franchuk': 'У Віті великій пеніс'
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        norm_text = normalize(update.message.text)
        for keyword, response in RESPONSES.items():
            if keyword in norm_text:
                await update.message.reply_text(response)
                return

def main():
    print("Startup..")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Рупіч готовий їбашить")
    app.run_polling()

if __name__ == '__main__':
    main()
