# Telegram Бот для Конвертации Валют

Этот простой Telegram бот предназначен для проверки текущих курсов обмена валют. Бот позволяет пользователям получить текущий обменный курс для USD и EUR в российских рублях (RUB). Это отличный пример для начинающих, желающих создать бота для Telegram с использованием Python.

## Начало Работы

Для начала работы с этим ботом вам нужно выполнить следующие шаги:

1. **Клонировать Репозиторий**

   Вы можете склонировать этот репозиторий с помощью следующей команды:

   ```bash
   git clone https://github.com/Svyat94/currency_bot.git
   ```

2. **Установить Зависимости**

   Убедитесь, что у вас установлен Python 3.x на вашей системе. Вы можете установить необходимые пакеты Python с помощью pip:

   ```bash
   pip install telebot
   pip install pycbrf
   pip install python-dotenv
   ```

3. **Создать Telegram Бота**

   Вам потребуется создать Telegram бота и получить токен API. Следуйте [официальной документации Telegram](https://core.telegram.org/bots#botfather), чтобы создать нового бота и получить ваш токен.

4. **Настроить Переменные Окружения**

   Создайте файл `.env` в директории проекта и добавьте в него токен вашего Telegram бота. Вы можете сделать это с помощью текстового редактора:

   ```bash
   YOUR_BOT_TOKEN="ваш_токен_бота_здесь"
   ```

5. **Запустить Бота**

   Вы можете запустить бота, выполните скрипт `main.py`:

   ```bash
   python main.py
   ```

6. **Взаимодействие с Ботом**

   Начните чат с вашим ботом в Telegram и введите `/start`, чтобы начать. Затем вы можете выбрать USD или EUR, чтобы получить текущий обменный курс.

## Команды Бота

- `/start`: Начинает разговор с ботом и отображает меню для выбора валюты.

## Особенности

- Предоставляет текущие курсы обмена для USD и EUR в RUB.
- Использует библиотеку [pycbrf](https://pypi.org/project/pycbrf/) для получения курсов валют.

## Автор

- Виноградов Святослав

## Благодарности

- Особая благодарность создателям библиотек [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) и [pycbrf](https://pypi.org/project/pycbrf/), благодаря которым этот проект стал возможным.
