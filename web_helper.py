import json
import requests
import readConfig

API_KEY = readConfig.getData('web_helper')
# print("Key: {}".format(API_KEY))

def get_stock_price(symbol):
    response = requests.get(f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}")
    return json.loads(response.text)

def get_crypto_price(symbol):
    response = requests.get(f"https://finnhub.io/api/v1/crypto/symbol={symbol}?exchange=binance&token={API_KEY}")
    print(response.text)
    return response
