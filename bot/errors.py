import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Telegram error handler."""
    logger.error("An error occurred while processing the update.", exc_info=context.error)

    if update:
        logger.error(f"Update that caused the error: {update}")
    if context.error:
        logger.error(f"Exception: {context.error}")

    if update and update.message:
        await update.message.reply_text("Something went wrong. Try again later.")