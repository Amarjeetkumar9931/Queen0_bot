import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👑 Welcome to Queen Chat Bot!\n\n"
        "❤️ Hello! Main aapka personal chatbot hoon.\n"
        "💬 Mujhse kuch bhi pooch sakte ho."
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(
        message,
        "🤖 Queen Chat Bot Commands:\n\n"
        "/start - Start Bot\n"
        "/help - Help\n"
        "/about - About Bot"
    )

@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, "👑 Queen Chat Bot\nMade with ❤️")

@bot.message_handler(func=lambda message: True)
def chat(message):
    bot.reply_to(
        message,
        "💖 Aapne kaha:\n" + message.text +
        "\n\nMain Queen Chat Bot hoon! 👑"
    )

bot.infinity_polling()
