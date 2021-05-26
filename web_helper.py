import json
import requests
import readConfig

API_KEY = readConfig.getData('web_helper')
# print("Key: {}".format(API_KEY))

def get_stock_price(symbol):
    response = requests.get("https://finnhub.io/api/v1/quote?symbol={}&token={}".format(symbol, API_KEY))
    return json.loads(response.text)

def get_crypto_price(symbol):
    response = requests.get("https://finnhub.io/api/v1/crypto/symbol={}?exchange=binance&token={}".format(symbol, API_KEY))
    print(response.text)
    return response
