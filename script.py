import logging
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Налаштування логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '8473734736:AAGSNU9MaiUorcOZw6zJM13OEyzpZV-jhrg'  # Заміни на свій токен

# Regex для ключових слів (толерантно до i/I, регістру)
RESPONSES = {
    r'[р][у][п][іі][ч]': 'РУПІЧ ЧМО!',     # "рупіч" / "rupich"
    r'[р][у][п][іі][з][я][н][а]': 'РУПІЧ ЧМО!',  # "рупізяна"
    r'[ф][р][а][н][ч][у][к]': 'У Віті великій пеніc'  # "франчук"
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        text = update.message.text
        for pattern, response in RESPONSES.items():
            if re.search(pattern, text, re.IGNORECASE):
                await update.message.reply_text(response)
                return

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == '__main__':
    main()
