import logging
import os
import requests
from django.template import Context
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
FORTNITE_API_KEY=os.getenv("FORTNITE_API_KEY")
FORTNITE_API_URL=os.getenv("FORTNITE_API_URL")
print(TELEGRAM_BOT_TOKEN, FORTNITE_API_KEY, FORTNITE_API_URL)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def split_message(text, max_length=4096):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

def trim_line(line):
    return line.split(" x ")[1].split("for")[0].strip()

async def get_fortnite_shop():
    headers = {'Authorization': FORTNITE_API_KEY}
    response = requests.get(FORTNITE_API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        items = data.get("data", {}).get("entries", [])
        if items:
            shop_text = "Fortnite Shop Items Today\n\n"
            for item in items:
                if 'offerTag' in item:
                    continue
                name = trim_line(item['devName'])
                shop_text += f"{name} - {item['finalPrice']} V-bucks\n"
            return shop_text if shop_text.strip() != "Fortnite Shop Items Today" else "No valid items in the shop today."
        else:
            return "Shop is empty or API did not return the data."
    else:
        return f"API error: {response.status_code}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi, I'm a Fortnite store tracking bot.")

async def shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    shop_info = await get_fortnite_shop()
    messages = split_message(shop_info)
    for msg in messages:
        await update.message.reply_text(msg)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="An error occurred while processing the update.", exc_info=context.error)

    if update and update.message:
        await update.message.reply_text("Something went wrong. Try again later.")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()


    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shop", shop))
    app.add_error_handler(error_handler)

    app.run_polling()

if __name__ == '__main__':
    main()