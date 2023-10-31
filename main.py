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
    markup = get_currency_keyboard()
    bot.send_message(
        chat_id=message.chat.id,
        text=f'<b>Привет {message.from_user.first_name} {message.from_user.last_name}! Выбери курс валют!</b>',
        reply_markup=markup, parse_mode='html'
    )

def get_currency_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    currencies = ['USD', 'EUR', 'CNY', 'KZT']
    
    for currency in currencies:
        itembtn = telebot.types.KeyboardButton(currency)
        markup.add(itembtn)
    
    return markup


@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur', 'cny', 'kzt']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(
            chat_id=message.chat.id,
            text=f'<b>Курс {message_norm.upper()} = {float(rates[message_norm.upper()].rate)} рублей</b>',
            parse_mode='html'
        )
    
    else:
        reply_text = "Пока я не умею распознавать такие команды, но мой создатель в скором времени все добавит. А пока вы можете посмотреть текущий курс интересующей вас валюты."
        markup = get_currency_keyboard()
        bot.send_message(
            chat_id=message.chat.id,
            text=reply_text,
            reply_markup=markup,
            parse_mode='html'
        )


bot.polling(non_stop=True)
