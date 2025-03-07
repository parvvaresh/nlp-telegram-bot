import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
from handlers.start_handler import start
from handlers.button_handler import button_handler
from utils.state import user_states

if not os.path.exists("downloads"):
    os.makedirs("downloads")

async def text_handler(update, context):
    chat_id = update.effective_chat.id
    if chat_id in user_states:
        service = user_states.pop(chat_id)
        if service == 'summarize':
            from services.text_summary import summarize_text
            result = summarize_text(update.message.text)
            await update.message.reply_text("خلاصه:\n" + result)
        elif service == 'detect_topic':
            from services.topic_detection import detect_topic
            result = detect_topic(update.message.text)
            await update.message.reply_text("موضوع احتمالی:\n" + result)
        else:
            await update.message.reply_text("لطفاً فایل PDF را ارسال کنید.")
    else:
        await update.message.reply_text('سلام! لطفاً یکی از گزینه‌ها را انتخاب کنید:\n\nبرای شروع /start را بفرستید.')

async def document_handler(update, context):
    chat_id = update.effective_chat.id
    if chat_id in user_states and user_states[chat_id] == 'extract_pdf':
         file = await update.message.document.get_file()
         file_path = os.path.join("downloads", update.message.document.file_name)
         await file.download_to_drive(file_path)
         from services.pdf_extractor import extract_text_from_pdf
         text = extract_text_from_pdf(file_path)
         await update.message.reply_text("متن استخراج شده:\n" + text)
         user_states.pop(chat_id)
    else:
         await update.message.reply_text("لطفاً ابتدا یکی از گزینه‌های موجود را انتخاب کنید.")


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))  # اینجا start باید async باشد
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    application.add_handler(MessageHandler(filters.Document.PDF, document_handler))

    application.run_polling()

if __name__ == '__main__':
    main()
