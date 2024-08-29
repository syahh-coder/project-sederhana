
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Mengaktifkan logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Fungsi yang akan dipanggil saat bot menerima perintah /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Halo! Saya adalah bot Telegram.')

# Fungsi yang akan dipanggil saat bot menerima pesan teks
async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("SAya Ukas")
async def hello(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("SAya Ukas")

async def link(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("dapatkan panduan python dengan klik link di bawah ini \nhttps://clicky.id/si-ukas/contekan-rumus-python-isi")

def main() -> None:
    # Token API yang didapat dari BotFather
    token = '7485964982:AAGsiPQ7P6hEFvhKrtShk_zfRLm8nxiBA0w'
    
    # Membuat Application
    application = Application.builder().token(token).build()

    # Mendaftarkan handler untuk perintah /start
    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("contekan", link))

    # Mendaftarkan handler untuk pesan teks
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Mulai bot
    application.run_polling()

if __name__ == '__main__':
    main()
