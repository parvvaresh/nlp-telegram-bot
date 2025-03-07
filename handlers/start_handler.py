from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("خلاصه سازی", callback_data='summarize')],
        [InlineKeyboardButton("استخراج PDF", callback_data='extract_pdf')],
        [InlineKeyboardButton("حدس تاپیک", callback_data='detect_topic')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text='سلام! لطفاً یکی از گزینه‌ها را انتخاب کنید:',
        reply_markup=reply_markup
    )
