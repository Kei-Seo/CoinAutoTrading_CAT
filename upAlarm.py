import time

import pybithumb

tickers = pybithumb.get_tickers()

print(tickers)
while True:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(1)
