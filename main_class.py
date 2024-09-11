import telebot
from telebot import types
import price_of_cryptocurrency
import requests
import threading

import api_key
import time

running = False
user_state = False
time_loop = float

TOKEN = api_key.API_telegram
bot = telebot.TeleBot(TOKEN)


def create_start_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_start = types.KeyboardButton('start menu')
    btn_live_price = types.KeyboardButton('live price')
    btn_live_price_loop = types.KeyboardButton('live price loop')
    btn_help = types.KeyboardButton('help')
    btn_info = types.KeyboardButton('info')
    btn_live_price_special_cryptocurrency = types.InlineKeyboardButton('live price special cryptocurrency')
    markup.add(btn_start, btn_live_price, btn_live_price_loop, btn_help, btn_info,
               btn_live_price_special_cryptocurrency)
    return markup


def break_loop():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_break = types.KeyboardButton('Break loop')
    markup.add(btn_break)
    return markup


def send_hello(chat_id):
    global running
    while running:
        prices = price_of_cryptocurrency.send_pricecryptocurrency_price()
        bot.send_message(chat_id, f"LIST:\n{prices}\n\nIf you want to stop Loop press button break")
        time.sleep(5)



@bot.message_handler(commands=['break'])
def stop(message):
    global user_stat
    global running
    user_stat = False
    if running:
        running = False
        bot.send_message(message.chat.id, f"The loop stopped\nOption: /start   /help   /info   /live_price  "
                                          f"/live_price_loop /live_price_special_cryptocurrency",reply_markup=create_start_button())


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_start = types.KeyboardButton('start menu')
    btn_live_price = types.KeyboardButton('live price'
                                          '')
    btn_live_price_loop = types.KeyboardButton('live price loop')
    btn_help = types.KeyboardButton('help')
    btn_info = types.KeyboardButton('info')
    btn_live_price_special_cryptocurrency = types.InlineKeyboardButton('live price special cryptocurrency')
    markup.add(btn_start, btn_live_price, btn_live_price_loop, btn_help, btn_info,
               btn_live_price_special_cryptocurrency)

    bot.send_message(message.chat.id, f"Hello 🗿,\nThis robot is designed to see the current prices of "
                                      f"cryptocurrencies.\n\nYou can see "
                                      f"list of the top 24 currencies on market by live price button\nOR\nenter "
                                      f"your currency name like ( btc ton xrp )\n\n", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global user_state
    if message.text == 'start menu':
        bot.send_message(message.chat.id, f"Hello 🗿,\nThis robot is designed to see the current prices of "
                                          f"cryptocurrencies.\n\nYou can see "
                                          f"list of the top 24 currencies on market by live price button\nOR\nenter "
                                          f"your currency name like ( btc ton xrp )\n\n")

    elif message.text == 'live price':
        # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # button3 = types.KeyboardButton('دکمه 3')
        # button4 = types.KeyboardButton('دکمه 4')
        # button5 = types.KeyboardButton('دکمه 5')
        # markup.add(button3, button4, button5)
        prices = price_of_cryptocurrency.send_pricecryptocurrency_price()
        bot.send_message(message.chat.id, f"LIST:\n{prices}")

    elif message.text == 'help':
        bot.reply_to(message, f"option:\n/start\t/info  /live_price  /live_price_loop  "
                              f"/live_price_special_cryptocurrency")
    elif message.text == 'info':
        bot.send_message(message.chat.id, text=f"This bot created by: Mohammad Amin Bajelan\n\nwith Telegram api.")

    elif message.text == 'live price loop':
        global running
        if not running:
            running = True
            bot.send_message(message.chat.id, "Start loop.", reply_markup=break_loop())
            thread = threading.Thread(target=send_hello, args=(message.chat.id,))
            thread.start()
    elif message.text == 'Break loop':
        stop(message)

    elif message.text == 'live price special cryptocurrency':
        bot.send_message(message.chat.id, text='Please entre name of your cryptocurrency like(btc ton xrp)',
                         reply_markup=break_loop())
        user_state = True

    else:
        name_of_token = str(message.text).upper()
        my_url = api_key.send_url(message)
        response = requests.get(url=my_url)

        if int(response.status_code) == 200 and user_state:
            bot.send_message(message, text="Your loop started.", reply_markup=break_loop())
            while user_state:
                token_price = float(response.json()['price'])
                token_price = str("{:.3f}".format(round(token_price, 4)))

                time.sleep(1)
                bot.send_message(message.chat.id,
                                 f"Current price of {name_of_token} equal:\n\n{name_of_token}   {token_price}\nfor "
                                 f"stop loop enter /break")
                time.sleep(10)

        elif int(response.status_code) >= 400:
            bot.reply_to(message, f"Something went wrong or this name is not dedicated 😢")
        else:
            token_price = float(response.json()['price'])
            token_price = str("{:.3f}".format(round(token_price, 4)))
            bot.reply_to(message, f"Current price of {name_of_token} equal:\n\n{name_of_token}   {token_price}")
            print(f"{message}   {token_price}")


bot.polling()
