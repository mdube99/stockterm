import json
import requests
from stock import Stock

comma = ","

def printStock(uinput, stockpicked):
    # Checks to see if the stock symbol exists (all prices will show as 0 if it doesn't)
    # If it doesn't it will return the main function
    # If the stock exists, it will print out the current price, daily high, daily low, and previous close
    if stockpicked.current_price == 0:
        print("\nUnknown stock, please try again.\n")
        return main()
    print(f"\n --- Stock information for {uinput} --- ")
    print(f"Current Price for {uinput}: {stockpicked.current_price}")
    print(f"Daily High for {uinput}: {stockpicked.daily_high}")
    print(f"Daily low for {uinput}: {stockpicked.daily_low}")
    print(f"Previous close for {uinput}: {stockpicked.previous_close}\n")

def main():
    uinput = str(input("What stock(s) would you like information for: "))
    # Checks to see if there are multiple stocks
    if comma in uinput:
        uinput = uinput.upper()
        multi_stock = uinput.split(",")
        for x in range(len(multi_stock)):
            # runs each stock in the list through a loop printing them
            stockpicked = Stock(multi_stock[x])
            stockpicked.update_stock()
            printStock(multi_stock[x], stockpicked)
    else:
    # If there aren't multiple stocks
        uinput = uinput.upper()
        stockpicked = Stock(uinput)
        stockpicked.update_stock()

        printStock(uinput, stockpicked)


if __name__ == "__main__":
    main()
