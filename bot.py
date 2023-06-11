
import telebot

BOT_TOKEN = "API key"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello butterfly, miss me?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Love You")

bot.infinity_polling()
