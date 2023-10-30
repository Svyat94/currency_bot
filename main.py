import os
from dotenv import load_dotenv
from datetime import datetime
import telebot
from pycbrf import ExchangeRates


load_dotenv()


YOUR_BOT_TOKEN = os.getenv("YOUR_BOT_TOKEN")
bot = telebot.TeleBot(YOUR_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')
    markup.add(itembtn1, itembtn2)
    bot.send_message(chat_id=message.chat.id, text='<b>Привет! Выбери курс валют!</b>', reply_markup=markup, parse_mode='html')

def user_name():
    pass

@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id, text=f'<b>Курс {message_norm.upper()} = {float(rates[message_norm.upper()].rate)} рублей</b>', parse_mode='html')

bot.polling(non_stop=True)
