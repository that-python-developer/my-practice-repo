import os
import telebot

API_KEY = '5324128381:AAH-KTHnk1nMPFKPwVqhBPn_ipd8_9RQP38'
bot = telebot.TeleBot(API_KEY)


def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")
  bot.send_message(message.chat.id, )

bot.polling()