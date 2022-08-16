import ccxt

with open("api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret  = lines[1].strip()

bitget = ccxt.bitget(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'option': {
        'defaultType': 'future'
    }
})

def open_order(exchange, symbol, amount, pivot):
    exchange.create_order(symbol, 'open', 'buy', amount, pivot - 500)


symbol = "SBTCSUSDT_SUMCBL"

markets = bitget.fetch_tickers()
print(markets)
