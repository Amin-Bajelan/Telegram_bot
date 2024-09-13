# package
import telebot
import time
import requests
from telebot import types
from datetime import datetime, timedelta

#classes
import price_of_cryptocurrency
import api_key

TOKEN = api_key.API_telegram
bot = telebot.TeleBot(TOKEN)

#flag for live price special cryptocurrency

flag_cryptocurrency = False
go_to_next_step = False
final_step = False
flag_while_cryptocurrency = False
flag = False  #for while loop

token_name = str
sleep_time = int

#flag for live price loop

flag_list_price = False
flag_loop = False

time_for_loop = int

#flag_look_for_another_cryptocurrency
flag_look_for_another_cryptocurrency = False


def stop_loop():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_stop = types.KeyboardButton('Stop')
    markup.add(btn_stop)
    return markup


def go_back():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_go_back = types.KeyboardButton('Back')
    markup.add(btn_go_back)
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
    btn_live_price_special_cryptocurrency = types.KeyboardButton('live price special cryptocurrency')
    btn_look_for_another = types.KeyboardButton('look for another cryptocurrency')
    markup.add(btn_start, btn_live_price, btn_live_price_loop, btn_help, btn_info,
               btn_live_price_special_cryptocurrency, btn_look_for_another)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_start = types.KeyboardButton('start menu')
    btn_live_price = types.KeyboardButton('live price')
    btn_live_price_loop = types.KeyboardButton('live price loop')
    btn_help = types.KeyboardButton('help')
    btn_info = types.KeyboardButton('info')
    btn_live_price_special_cryptocurrency = types.KeyboardButton('live price special cryptocurrency')
    btn_look_for_another = types.KeyboardButton('look for another cryptocurrency')
    markup.add(btn_start, btn_live_price, btn_live_price_loop, btn_help, btn_info,
               btn_live_price_special_cryptocurrency, btn_look_for_another)

    bot.send_message(message.chat.id, f"Hello 🗿,\nThis robot is designed to see the current prices of "
                                      f"cryptocurrencies.\n\nYou can see "
                                      f"list of the top 24 currencies on market by live price button\nOR\nenter "
                                      f"your currency name like ( btc ton xrp )\n\n", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # flag for live price special cryptocurrency
    global flag_while_cryptocurrency
    global flag_cryptocurrency
    global go_to_next_step
    global final_step
    global flag

    global token_name
    global sleep_time

    # flag for live price loop
    global flag_list_price
    global flag_loop

    global time_for_loop

    #for look for another cryptocurrency
    global flag_look_for_another_cryptocurrency

    if message.text == 'start menu':
        bot.send_message(message.chat.id, f"Hello 🗿,\nThis robot is designed to see the current prices of "
                                          f"cryptocurrencies.\n\nYou can see "
                                          f"list of the top 24 currencies on market by live price button\nOR\nenter "
                                          f"your currency name like ( btc ton xrp )\n\n")

    elif message.text == 'Cancel' or message.text == 'Stop' or message.text == 'Back':
        bot.send_message(message.chat.id, text="You back to default state: ", reply_markup=create_start_button())
        flag_while_cryptocurrency = False
        flag_cryptocurrency = False
        go_to_next_step = False
        final_step = False
        flag = False

        flag_list_price = False
        flag_loop = False


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
        flag_list_price = True

    if flag_list_price and message.text.isdigit():
        time_for_loop = int(message.text)
        flag_loop = True

        current_date = datetime.today()
        new_date = current_date + timedelta(minutes=time_for_loop)
        bot.send_message(message.chat.id, text=f"Your loop started: ", reply_markup=stop_loop())

        while flag_loop:
            time.sleep(10)
            current_date = datetime.today()
            if current_date >= new_date:
                new_date = current_date + timedelta(minutes=time_for_loop)
                prices = price_of_cryptocurrency.send_cryptocurrency_price()
                bot.send_message(message.chat.id, f"LIST:\n{prices}")
            else:
                print("not yet")
                print(current_date)
                print(new_date)


    elif message.text == 'live price special cryptocurrency':
        bot.send_message(message.chat.id, text=f"Please select your cryptocurrency: ",
                         reply_markup=create_button_cryptocurrency_name())
        flag_cryptocurrency = True

    if message.text == 'BTC' or message.text == 'ETH' or message.text == 'LTC' or message.text == 'XRP' or message.text == 'BCH' or message.text == 'BNB' or message.text == 'EOS' or message.text == 'XLM' or message.text == 'ETC' or message.text == 'TRX':
        token_name = message.text

        bot.send_message(message.chat.id, text=f"Please select your time: ", reply_markup=create_button_time())
        go_to_next_step = True

    if message.text.isdigit() and flag_cryptocurrency:
        sleep_time = message.text

        final_step = True
    if final_step:
        bot.send_message(message.chat.id, text=f"your loop started. ", reply_markup=stop_loop())
        print(token_name)
        print(sleep_time)
        name_of_token = token_name.upper()
        my_url = api_key.send_url(token_name)
        response = requests.get(url=my_url)
        print(my_url)

        print(my_url)

        token_price = float(response.json()['price'])
        token_price = str("{:.3f}".format(round(token_price, 4)))
        bot.send_message(message.chat.id,
                         f"Current price of {name_of_token} equal:\n\n{name_of_token}   {token_price}\nfor "
                         f"stop loop press stop button")

        sleep_time_minute = int(sleep_time)
        sleep_time = int(sleep_time) * 60
        current_date = datetime.today()
        new_date = current_date + timedelta(minutes=sleep_time_minute)
        print(current_date)
        print(new_date)

        flag = True
        while flag:
            time.sleep(10)
            current_date = datetime.today()
            if current_date >= new_date:
                new_date = current_date + timedelta(minutes=sleep_time_minute)
                token_price = float(response.json()['price'])
                token_price = str("{:.3f}".format(round(token_price, 4)))
                bot.send_message(message.chat.id,
                                 f"Current price of {name_of_token} equal:\n\n{name_of_token}   {token_price}\nfor "
                                 f"stop loop press button stop")
            else:
                print('\nnot yet')
                print(current_date)
                print(new_date)

    if message.text == 'look for another cryptocurrency':
        bot.send_message(message.chat.id, text=f"Please enter symbol of your cryptocurrency like (btc, xrp, ton): ",
                         reply_markup=go_back())
        flag_look_for_another_cryptocurrency = True


    else:
        name_of_token = str(message.text).upper()
        my_url = api_key.send_url(message.text)
        response = requests.get(url=my_url)
        if response.status_code == 200 and flag_look_for_another_cryptocurrency:
            print(message.text)
            token_price = float(response.json()['price'])
            token_price = str("{:.3f}".format(round(token_price, 4)))
            bot.send_message(message.chat.id,
                             f"Current price of {name_of_token} equal:\n\n{name_of_token}   {token_price}\nfor go to first step press button back: ")


bot.polling()
