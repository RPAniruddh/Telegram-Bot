
import telebot

BOT_TOKEN = "6041864624:AAFReQOhADKI7-gkA49AIBDiZdOhag2j_aU"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello butterfly, miss me?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Love You")

bot.infinity_polling()