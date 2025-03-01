import logging
from telegram.ext import Application, CommandHandler
from bot.config import TELEGRAM_BOT_TOKEN
from bot.handlers.start import start
from bot.handlers.summarize import summarize_command

# تنظیم logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # ثبت هندلرها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("summarize", summarize_command))

    # اجرای بات با استفاده از polling
    application.run_polling()

if __name__ == '__main__':
    main()
