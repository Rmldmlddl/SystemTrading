#!/usr/bin/python

from ..client import Client
from ..consts import *


class OrderApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    '''
    place an order
    price: Required for price limit  
    marginCoin: Margin currency
    size: When the price is limited, it is the quantity. The market price is bought as the quota.
    side：open_long open_short close_long close_short
    orderType: limit (limit price) market (market price)
    timeInForceValue: normal (normal limit order) 
                      postOnly (only for maker, the market price is not allowed to use this) 
                      ioc (immediately executed and cancel the remaining) 
                      fok (all executed or immediately canceled)
    presetTakeProfitPrice: Default Take Profit Price
    presetStopLossPrice： Preset stop loss price
    :return:
    '''
    def place_order(self, symbol, marginCoin, size, side, orderType, price='', clientOrderId='', timeInForceValue='normal', presetTakeProfitPrice='', presetStopLossPrice=''):
        params = {}
        if symbol and marginCoin and side and orderType and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["price"] = price
            params["size"] = size
            params["side"] = side
            params["orderType"] = orderType
            params["timeInForceValue"] = timeInForceValue
            params["clientOid"] = clientOrderId
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/placeOrder', params)
        else:
            return "pls check args "

    '''
    Order in bulk
    price: Required for price limit
    marginCoin: Margin currency
    order_data: 
    size: When the price is limited, it is the quantity. The market price is bought as the quota.
    side：open_long open_short close_long close_short
    orderType: limit (limit price) market (market price)
    timeInForceValue: normal (normal limit order) 
                      postOnly (only for maker, the market price is not allowed to use this) 
                      ioc (immediately executed and cancel the remaining) 
                      fok (all executed or immediately canceled)
    presetTakeProfitPrice: Default Take Profit Price
    presetStopLossPrice： Preset stop loss price
    :return:
    '''
    def batch_orders(self, symbol, marginCoin, order_data):
        params = {'symbol': symbol, 'marginCoin': marginCoin, 'orderDataList': order_data}
        return self._request_with_params(POST, MIX_ORDER_V1_URL + '/batch-orders', params)

    '''
    Cancellation
    :return:
    '''
    def cancel_orders(self, symbol, marginCoin, orderId):
        params = {}
        if symbol and orderId:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-order', params)
        else:
            return "pls check args "

    '''
    Cancellation in bulk
    orderIds: List 
    :return:
    '''
    def cancel_batch_orders(self, symbol, marginCoin, orderIds):
        if symbol and orderIds:
            params = {'symbol': symbol, 'marginCoin':marginCoin, 'orderIds': orderIds}
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-batch-orders', params)
        else:
            return "pls check args "

    '''
    Get order information
    :return:
    '''
    def detail(self, symbol, orderId):
        params = {}
        if symbol and orderId:
            params["symbol"] = symbol
            params["orderId"] = orderId
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/detail', params)
        else:
            return "pls check args "

    '''
    Get current order
    :return:
    '''
    def current(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/current', params)
        else:
            return "pls check args "

    '''
    Get historical orders
    isPre： 是否查询上一页
    :return:
    '''
    def history(self, symbol, startTime, endTime, pageSize, lastEndId='', isPre=False):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["isPre"] = isPre
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/history', params)
        else:
            return "pls check args "

    '''
    Get transaction details
    :return:
    '''
    def fills(self, symbol='', orderId=''):
        params = {}
        if symbol and orderId:
            params["symbol"] = symbol
            params["orderId"] = orderId
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/fills', params)
        else:
            return "pls check args "