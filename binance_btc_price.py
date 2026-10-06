import ccxt

exchange = ccxt.binance()
# 시세 조회 전용 공개 엔드포인트 (지역 제한이 덜함)
exchange.urls["api"]["public"] = "https://data-api.binance.vision/api/v3"
ticker = exchange.fetch_ticker("BTC/USDT")
print(f"Binance BTC/USDT 현재가: {ticker['last']:,.2f} USDT")
