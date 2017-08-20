import config
import telebot

import requests
import json
bot = telebot.TeleBot(config.token)
class WeatherBot:
    @bot.message_handler(commands=['start'])
    def start(message):
        sent = bot.send_message(message.chat.id, 'What do you want?')


    @bot.message_handler(commands=['weather'])
    def weather(message):
        bot.send_message(message.chat.id, "print a city")
        bot.register_next_step_handler(message, weather_1)

    def weather_1(message):
        city = message
        for a in  config.weather(city):
            bot.send_message(message.chat.id, a)

c = WeatherBot()

if  __name__ == '__main__' :
    bot.polling(none_stop = True)
