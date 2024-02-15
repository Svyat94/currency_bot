import os
from dotenv import load_dotenv
from datetime import datetime
import telebot
from pycbrf import ExchangeRates


load_dotenv()


YOUR_BOT_TOKEN = os.getenv("YOUR_BOT_TOKEN")
bot = telebot.TeleBot(YOUR_BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = get_currency_keyboard()

    bot.send_message(
        chat_id=message.chat.id,
        text=f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}! Я Бот, который тебе поможет с конвертацие валют. Выбери предложенный курс!</b>",
        reply_markup=markup,
        parse_mode="html",
    )


def get_currency_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    currencies = ["USD", "EUR", "CNY", "KZT"]

    for currency in currencies:
        itembtn = telebot.types.KeyboardButton(currency)
        markup.add(itembtn)

    return markup


@bot.message_handler(content_types=["text"])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ["usd", "eur", "cny", "kzt"]:
        rates = ExchangeRates(datetime.now())
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(
            chat_id=message.chat.id,
            text=f"<b>Курс {message_norm.upper()} = {float(rates[message_norm.upper()].rate)} рублей</b>",
            reply_markup=markup,
            parse_mode="html",
        )
        bot.send_message(
            chat_id=message.chat.id,
            text="Введите сумму для конвертации:",
        )
        bot.register_next_step_handler(message, convert_currency, message_norm)

    elif message_norm in ["помощь", "/help"]:
        help_text = """
        <b>Список команд:</b>

        /start - Начать работу с ботом
        /help - Вывести список команд

        <b>Конвертация валют:</b>

        Для конвертации валюты введите ее код (например, USD, EUR, CNY, KZT).
        Бот отправит вам текущий курс выбранной валюты по отношению к рублю.

        <b>Ввод суммы для конвертации:</b>

        После получения курса валюты введите сумму, которую хотите конвертировать.
        Бот пересчитает сумму в рубли и отправит вам результат.

        <b>Возврат к выбору валют:</b>

        После конвертации валюты нажмите на любую кнопку с кодом валюты, чтобы вернуться к выбору валют.
        """
        bot.send_message(
            chat_id=message.chat.id,
            text=help_text,
            parse_mode="html",
        )

    else:
        reply_text = (
            "Я не понимаю такую команду. Введите /help, чтобы увидеть список команд."
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=reply_text,
        )


def convert_currency(message, currency):
    try:
        amount = float(message.text)
        rates = ExchangeRates(datetime.now())
        converted_amount = amount * float(rates[currency.upper()].rate)
        bot.send_message(
            chat_id=message.chat.id,
            text=f"<b>{amount} {currency.upper()} = {converted_amount:.2f} рублей</b>",
            parse_mode="html",
        )
        markup = get_currency_keyboard()
        bot.send_message(
            chat_id=message.chat.id,
            text="Если хотите выбрать другую валюту для конвертации нажмите в меню желаемой код валюты или нажмите /help для помощи.",
            reply_markup=markup,
            parse_mode="html",
        )
    except ValueError:
        bot.send_message(
            chat_id=message.chat.id,
            text="Введите корректную сумму для конвертации.",
        )


bot.polling(non_stop=True)
