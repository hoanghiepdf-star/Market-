"""
Telegram Bot - Entry point
Services: Telegram Bot • Website • Mobile App
"""

import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text(
        "🤖 Bot is running 🚀\n\n"
        "💻 Website Design\n"
        "📱 Mobile App Design\n"
        "⚙️ Custom Bot & Automation\n\n"
        "📩 Contact to build your idea."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
