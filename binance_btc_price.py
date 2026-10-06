import ccxt

exchange = ccxt.binance()
# 시세 조회 전용 공개 엔드포인트 (지역 제한이 덜함)
exchange.urls["api"]["public"] = "https://data-api.binance.vision/api/v3"
# fetch_ticker는 내부에서 선물(fapi) 시장 목록까지 불러와 지역 제한(451)에 걸리므로
# 현물 가격 조회 API를 직접 호출한다.
ticker = exchange.publicGetTickerPrice({"symbol": "BTCUSDT"})
print(f"Binance BTC/USDT 현재가: {float(ticker['price']):,.2f} USDT")
