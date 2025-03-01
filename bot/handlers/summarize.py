from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.summarizer import summarize_text

async def summarize_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if context.args:
        processing_message = await update.message.reply_text("در حال پردازش...")
        text = " ".join(context.args)
        summary = summarize_text(text, num_sentences=3)
        await processing_message.edit_text(summary)
    else:
        await update.message.reply_text("لطفاً متن را به همراه دستور /summarize وارد کنید.")
