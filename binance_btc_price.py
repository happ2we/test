import ccxt

exchange = ccxt.binance()
ticker = exchange.fetch_ticker("BTC/USDT")
print(f"Binance BTC/USDT 현재가: {ticker['last']:,.2f} USDT")
