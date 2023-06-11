
import telebot

BOT_TOKEN = "API key"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello there")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Not valid")

bot.infinity_polling()
