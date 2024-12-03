import logging
from telegram.ext import Application, CommandHandler
from config.settings import TELEGRAM_BOT_TOKEN
from bot.handlers import start, shop
from bot.errors import error_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    try:
        app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("shop", shop))
        app.add_error_handler(error_handler)

        logger.info("Bot is running.")
        app.run_polling()
    except Exception as e:
        logger.error(f"Application running error: {e}")

if __name__ == '__main__':
    main()