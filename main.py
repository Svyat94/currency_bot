import os
from dotenv import load_dotenv
from datetime import datetime
import telebot
from pycbrf import ExchangeRates
from datetime import datetime, timedelta


load_dotenv()


YOUR_BOT_TOKEN = os.getenv("YOUR_BOT_TOKEN")
bot = telebot.TeleBot(YOUR_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')
    itembtn3 = telebot.types.KeyboardButton('CNY')
    itembtn4 = telebot.types.KeyboardButton('KZT')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(chat_id=message.chat.id, text=f'<b>Привет {message.from_user.first_name} {message.from_user.last_name}! Выбери курс валют!</b>', reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur', 'cny', 'kzt']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id, text=f'<b>Курс {message_norm.upper()} = {float(rates[message_norm.upper()].rate)} рублей</b>', parse_mode='html')
    
    else:
        reply_text = "Пока я не умею распознавать такие команды, но мой создатель в скором времени все добавит. А пока вы можете посмотреть текущий курс интересующей вас валюты."
        markup = get_currency_keyboard()
        bot.send_message(chat_id=message.chat.id, text=reply_text, reply_markup=markup, parse_mode='html')

def get_currency_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')
    itembtn3 = telebot.types.KeyboardButton('CNY')
    itembtn4 = telebot.types.KeyboardButton('KZT')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return markup


bot.polling(non_stop=True)
