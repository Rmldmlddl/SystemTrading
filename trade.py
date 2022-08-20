import bitget.mix.market_api as market
import bitget.mix.account_api as accounts
import bitget.mix.position_api as position
import bitget.mix.order_api as order
import bitget.mix.plan_api as plan
import bitget.mix.trace_api as trace
import json
import time

with open("api.txt") as f:
    lines = f.readlines()
    api_key    = lines[0].strip()
    secret     = lines[1].strip()
    passphrase = lines[2].strip()

symbol = "SBTCSPERP_SCMCBL"
marginCoin = "SUSDC"
productType = "scmcbl"
price_gap = 500
order_size = 0.0003

marketApi = market.MarketApi(api_key, secret, passphrase, use_server_time=False, first=False)
orderApi = order.OrderApi(api_key, secret, passphrase, use_server_time=False, first=False)
accountApi = accounts.AccountApi(api_key, secret, passphrase, use_server_time=False, first=False)
positionApi = position.PositionApi(api_key, secret, passphrase, use_server_time=False, first=False)

'''
result = orderApi.place_order(symbol, marginCoin='SUSDC', size=0.001, side='open_long', orderType='limit', price='22100')
orderID = result['data']['orderId']
print(orderID)

detail = orderApi.detail(symbol, orderID)
'''

# Size balancing
account = accountApi.account(symbol, marginCoin)
first_order_size = float(account['data']['btcEquity']) * 0.4

# First Order
first_long_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=first_order_size,
                                        side='open_long', orderType='market')
first_short_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=first_order_size,
                                        side='open_short', orderType='market')

first_long_orderID = first_long_order['data']['orderId']
first_short_orderID = first_short_order['data']['orderId']

# Calculate pivot price
position_info = positionApi.all_position(productType=productType, marginCoin=marginCoin)
first_long_price = position_info['data'][0]['averageOpenPrice']
first_short_price = position_info['data'][1]['averageOpenPrice']

pivot_price = int(float(first_long_price) + float(first_short_price)) / 2

# First limit order
upper_price = str(pivot_price + price_gap)
lower_price = str(pivot_price - price_gap)

print(upper_price + '\n')
print(lower_price + '\n')

upper_open_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                        side='open_short', orderType='limit', price=upper_price)
upper_close_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                        side='close_long', orderType='limit', price=upper_price)

lower_open_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                        side='open_long', orderType='limit', price=lower_price)
lower_close_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                        side='close_short', orderType='limit', price=lower_price)

upper_open_orderID = upper_open_order['data']['orderId']
upper_close_orderID = upper_close_order['data']['orderId']
lower_open_orderID = lower_open_order['data']['orderId']
lower_close_orderID = lower_close_order['data']['orderId']

# Loop
while True:
    # update order info
    upper_open_order_info = orderApi.detail(symbol=symbol, orderId=upper_open_orderID)
    upper_close_order_info = orderApi.detail(symbol=symbol, orderId=upper_close_orderID)
    lower_open_order_info = orderApi.detail(symbol=symbol, orderId=lower_open_orderID)
    lower_close_order_info = orderApi.detail(symbol=symbol, orderId=lower_close_orderID)

    # upper order filled
    if upper_open_order_info['data']['state'] == 'filled' and upper_close_order_info['data']['state'] == 'filled':
        # update price
        pivot_price = float(upper_price)
        upper_price = str(pivot_price + price_gap)
        lower_price = str(pivot_price - price_gap)

        # cancel previous lower order
        orderApi.cancel_orders(symbol=symbol, marginCoin=marginCoin, orderId=lower_open_orderID)
        orderApi.cancel_orders(symbol=symbol, marginCoin=marginCoin, orderId=lower_close_orderID)

        # make order
        upper_open_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                                side='open_short', orderType='limit', price=upper_price)
        upper_close_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                                 side='close_long', orderType='limit', price=upper_price)

        lower_open_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                                side='open_long', orderType='limit', price=lower_price)
        lower_close_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                                 side='close_short', orderType='limit', price=lower_price)

        # update orderID
        upper_open_orderID = upper_open_order['data']['orderId']
        upper_close_orderID = upper_close_order['data']['orderId']
        lower_open_orderID = lower_open_order['data']['orderId']
        lower_close_orderID = lower_close_order['data']['orderId']

    # lower order filled
    elif lower_open_order_info['data']['state'] == 'filled' and lower_close_order_info['data']['state'] == 'filled':
        # update price
        pivot_price = float(lower_price)
        upper_price = str(pivot_price + price_gap)
        lower_price = str(pivot_price - price_gap)

        # cancel previous upper order
        orderApi.cancel_orders(symbol=symbol, marginCoin=marginCoin, orderId=upper_open_orderID)
        orderApi.cancel_orders(symbol=symbol, marginCoin=marginCoin, orderId=upper_close_orderID)

        # make order
        upper_open_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                                side='open_short', orderType='limit', price=upper_price)
        upper_close_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                                 side='close_long', orderType='limit', price=upper_price)

        lower_open_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                                side='open_long', orderType='limit', price=lower_price)
        lower_close_order = orderApi.place_order(symbol=symbol, marginCoin=marginCoin, size=order_size,
                                                 side='close_short', orderType='limit', price=lower_price)

        # update orderID
        upper_open_orderID = upper_open_order['data']['orderId']
        upper_close_orderID = upper_close_order['data']['orderId']
        lower_open_orderID = lower_open_order['data']['orderId']
        lower_close_orderID = lower_close_order['data']['orderId']

    time.sleep(2)
