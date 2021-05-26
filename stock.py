import json
import web_helper

class Stock():
    "Pulls from web_helper.api to get stock information"

    last_updated = 0
    current_price = 0
    daily_high = 0
    daily_low = 0
    json = ""
    symbol = "BLANK"

    def __init__(self, symbol):
        self.symbol = symbol


    def update_stock(self):
        response = web_helper.get_stock_price(self.symbol)
        # print(response)
        self.json = response
        self.current_price = response["c"]
        self.daily_high = response["h"]
        self.daily_low = response["l"]