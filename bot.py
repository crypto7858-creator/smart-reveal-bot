from telegram.request import HTTPXRequest
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Smart Reveal Bot is running!")

request = HTTPXRequest(
    proxy="socks5://127.0.0.1:1080"
)

app = Application.builder().token(TOKEN).request(request).build()

app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()