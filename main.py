import json
import requests
import time
from stock import Stock

def main():

    uinput = str(input("What stock would you like information for: "))
    stockpicked = Stock(uinput.upper())
    stockpicked.update_stock()
    print(f" --- Stock information for {uinput.upper()}--- ")
    print(f"Current Price for {uinput.upper()}: {stockpicked.current_price}")
    print(f"Daily High for {uinput.upper()}: {stockpicked.daily_high}")
    print(f"Daily low for {uinput.upper()}: {stockpicked.daily_low}")



if __name__ == "__main__":
    main()
