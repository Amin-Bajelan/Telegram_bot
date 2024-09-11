import api_key
import requests
import json


def send_pricecryptocurrency_price():
    my_url = api_key.url_coinmarketcap
    my_json = requests.get(my_url, params=api_key.parameters, headers=api_key.headers).json()
    my_str = ''
    coins = my_json['data']

    for x in coins:
        token = x['symbol']

        if token == str('SHIB'):
            price = (x['quote']['USD']['price'])
            a = float(price * 100000)
            print(f"{token}     ", "{:.3f}".format(round(a, 4)))
            final_token_name = str(token)
            final_token_price = str("{:.3f}".format(round(a, 4)))

        else:
            price = float(x['quote']['USD']['price'])
            print(f"{token}    ", "{:.3f}".format(round(price, 4)))
            final_token_name = str(token)
            final_token_price = str("{:.3f}".format(round(price, 4)))
            print(final_token_name, final_token_price)

        my_str = my_str + f"\n{final_token_name}   {final_token_price}\n"
    return my_str
