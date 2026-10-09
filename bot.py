import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🎉 স্বাগতম Smart Income Bot-এ!\n\n"
        "📌 /tasks — কাজ দেখুন\n"
        "💰 /balance — পয়েন্ট দেখুন\n"
        "ℹ️ /help — সাহায্য"
    )

@bot.message_handler(commands=["tasks"])
def tasks(message):
    bot.reply_to(
        message,
        "📋 পরীক্ষামূলক কাজ:\n"
        "১. বটের /start কমান্ড ব্যবহার করুন\n"
        "২. /
