from telegram import Update
from telegram.ext import CallbackContext
from utils.state import user_states

async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    service = query.data
    chat_id = query.message.chat_id
    user_states[chat_id] = service

    if service == 'summarize':
        await query.edit_message_text(text="لطفاً متنی که می‌خواهید خلاصه شود را ارسال کنید:")
    elif service == 'extract_pdf':
        await query.edit_message_text(text="لطفاً فایل PDF مورد نظر خود را ارسال کنید:")
    elif service == 'detect_topic':
        await query.edit_message_text(text="لطفاً متنی که می‌خواهید موضوع آن حدس زده شود را ارسال کنید:")
    else:
        await query.edit_message_text(text="سرویس ناشناخته.")
