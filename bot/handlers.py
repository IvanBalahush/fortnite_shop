from telegram import Update
from telegram.ext import ContextTypes

from fortnite_shop.bot.shop import get_fortnite_shop
from fortnite_shop.bot.utils import split_message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/start command handler."""
    await update.message.reply_text("Hi, I'm a Fortnite shop tracking bot.")

async def shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/shop command handler."""
    shop_info = await get_fortnite_shop()
    messages = split_message(shop_info)
    for msg in messages:
        await update.message.reply_text(msg)
