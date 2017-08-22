import config
import telebot
import requests
import json
import os
from telegram.ext import Updater, CommandHandler
bot = telebot.TeleBot(config.token)
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(config.token)

updater.dispatcher.add_handler(CommandHandler('start', start))

def start(self, update):
	sent = bot.send_message(message.chat.id, 'What do you want?')
	
updater.dispatcher.add_handler(CommandHandler('weather', start))
		
def weather(self, update):
	bot.send_message(message.chat.id, "print a city")
	bot.register_next_step_handler(message, weather_1)
		
def weather_1(self, update):
	city = update.message
	for a in  config.weather(city):
		bot.send_message(message.chat.id, a)

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://weatherbot.herokuapp.com/" + TOKEN)
updater.idle()
