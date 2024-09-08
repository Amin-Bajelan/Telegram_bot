import threading

import telebot
from telebot import types
import requests
import price_of_cryptocurrency
import time

import api_key

bot = telebot.TeleBot(token=api_key.API_telegram, parse_mode=None)

running = False
user_stat = False


def send_hello(chat_id):
    global running
    while running:
        bot.send_message(chat_id, f"LIST:\n{price_of_cryptocurrency.my_str}\n\nIf you want to stop Loop:\n\n/break")
        time.sleep(5)


@bot.message_handler(commands=['live_price_loop'])
def start(message):
    global running
    if not running:
        running = True
        bot.send_message(message.chat.id, "Start loop.")
        thread = threading.Thread(target=send_hello, args=(message.chat.id,))
        thread.start()


@bot.message_handler(commands=['break'])
def stop(message):
    global user_stat
    global running
    user_stat = False
    if running:
        running = False
        bot.send_message(message.chat.id, f"The loop stopped\nOption: /start   /help   /info   /live_price  "
                                          f"/live_price_loop /live_price_special_cryptocurrency")


@bot.message_handler(commands=['live_price_special_cryptocurrency'])
def start_loop(message):
    bot.reply_to(message, "Please enter name of your cryptocurrency like(btc ton xrp)")
    global user_stat
    user_stat = True


@bot.message_handler(['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=7)
    btn_live_price = types.KeyboardButton('live_price')
    btn_live_price_loop = types.KeyboardButton('live price loop')
    btn_info = types.KeyboardButton('info')
    btn_help = types.KeyboardButton('help')

    markup.add(btn_live_price_loop, btn_live_price, btn_info, btn_help)
    if message.text == '/start':
        bot.reply_to(message,
                     f"Hello 🗿,\nThis robot is designed to see the current prices of cryptocurrencies.\n\nYou can see "
                     f"list of the top 24 currencies on market\nOR\nenter "
                     f"your currency name like ( btc ton xrp )\n\n /live_price   "
                     f"/help   /info    /live_price_loop    /live_price_special_cryptocurrency\n\nor you can enter name:")



    elif message.text == 'live_price':
        bot.reply_to(message, f"LIST:\n{price_of_cryptocurrency.my_str}")
    elif message.text == 'help':
        bot.reply_to(message, f"option:\n/start\t/info  /live_price  /live_price_loop  "
                              f"/live_price_special_cryptocurrency")
    elif message.text == 'info':
        bot.reply_to(message, f"This bot created by: Mohammad Amin Bajelan\n"

                              f"with Telegram api.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    name_of_token = str(message.text).upper()
    my_url = api_key.send_url(message)
    response = requests.get(url=my_url)

    if int(response.status_code) == 200 and user_stat:
        bot.reply_to(message, text="Your loop started.")
        while user_stat:
            token_price = float(response.json()['price'])
            token_price = str("{:.3f}".format(round(token_price, 4)))

            time.sleep(1)
            bot.send_message(message.chat.id,
                             f"Current price of {name_of_token} equal:\n\n{name_of_token}   {token_price}\nfor stop loop enter /break")
            time.sleep(10)

    elif int(response.status_code) >= 400:
        bot.reply_to(message, f"Something went wrong or this name is not dedicated 😢")
    else:
        token_price = float(response.json()['price'])
        token_price = str("{:.3f}".format(round(token_price, 4)))
        bot.reply_to(message, f"Current price of {name_of_token} equal:\n\n{name_of_token}   {token_price}")
        print(f"{message}   {token_price}")


bot.infinity_polling()
