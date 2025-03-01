from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "سلام! من یک بات خلاصه‌سازی هستم. از دستور /summarize به همراه متن مورد نظر خود استفاده کنید."
    )
