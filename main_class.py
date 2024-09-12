# timedelta
import telebot
from telebot import types
import datetime
import api_key
import time
import requests
import price_of_cryptocurrency

TOKEN = api_key.API_telegram
bot = telebot.TeleBot(TOKEN)

continue_state = True
flag = True


def stop_loop():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_stop = types.KeyboardButton('Stop')
    markup.add(btn_stop)
    return markup


def create_button_cryptocurrency_name():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_btc = types.KeyboardButton('BTC')
    btn_eth = types.KeyboardButton('ETH')
    btn_ltc = types.KeyboardButton('LTC')
    btn_xrp = types.KeyboardButton('XRP')
    btn_bch = types.KeyboardButton('BCH')
    btn_bnb = types.KeyboardButton('BNB')
    btn_eos = types.KeyboardButton('EOS')
    btn_xlm = types.KeyboardButton('XLM')
    btn_etc = types.KeyboardButton('ETC')
    btn_trx = types.KeyboardButton('TRX')
    btn_cancel = types.KeyboardButton('Cancel')
    markup.add(btn_btc, btn_eth, btn_ltc, btn_xrp, btn_bch, btn_bnb, btn_eos, btn_xlm, btn_etc, btn_trx, btn_cancel)
    return markup


def create_button_time():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_5 = types.KeyboardButton('5')
    btn_15 = types.KeyboardButton('15')
    btn_30 = types.KeyboardButton('30')
    btn_60 = types.KeyboardButton('60')
    btn_cancel = types.KeyboardButton('Cancel')
    markup.add(btn_5, btn_15, btn_30, btn_60, btn_cancel)
    return markup


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


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_start = types.KeyboardButton('start menu')
    btn_live_price = types.KeyboardButton('live price')
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
    global check_name
    global check_time
    global timer_for_loop
    global continue_state

    if message.text == 'start menu':
        bot.send_message(message.chat.id, f"Hello 🗿,\nThis robot is designed to see the current prices of "
                                          f"cryptocurrencies.\n\nYou can see "
                                          f"list of the top 24 currencies on market by live price button\nOR\nenter "
                                          f"your currency name like ( btc ton xrp )\n\n")

    elif message.text == 'Cancel':
        bot.send_message(message.chat.id, text="You back to default state: ", reply_markup=create_start_button())

    elif message.text == 'live price':
        prices = price_of_cryptocurrency.send_cryptocurrency_price()
        bot.send_message(message.chat.id, f"LIST:\n{prices}")

    elif message.text == 'help':
        bot.send_message(message.chat.id, f"option:\n/start\t/info  /live_price  /live_price_loop  "
                                          f"/live_price_special_cryptocurrency")
    elif message.text == 'info':
        bot.send_message(message.chat.id, text=f"This bot created by: Mohammad Amin Bajelan\n\nwith Telegram api.")

    elif message.text == 'live price loop':
        bot.send_message(message.chat.id, text=f"Please select time of your cryptocurrency loop: ",
                         reply_markup=create_button_time())


    elif message.text == 'Stop':
        create_start_button()

    elif message.text == 'live price special cryptocurrency':
        bot.send_message(message.chat.id, text=f"Please enter your cryptocurrency symbol like ( btc ton xrp ):",
                         reply_markup=create_button_cryptocurrency_name())


    elif message.text.isdigit() == True:


    if continue_state == True:
        name_of_token = str(message.text).upper()
        my_url = api_key.send_url(message)
        response = requests.get(url=my_url)
        token_price = float(response.json()['price'])
        token_price = str("{:.3f}".format(round(token_price, 4)))
        bot.send_message(message.chat.id,
                         f"Current price of {name_of_token} equal:\n\n{name_of_token}  {token_price}\nfor "
                         f"stop loop enter /break")


bot.polling()
