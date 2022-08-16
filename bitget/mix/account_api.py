#!/usr/bin/python

from ..client import Client
from ..consts import *


class AccountApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    '''
    load user account info
    symbol: 合约交易对
    marginCoin: margin currency(ex. USDT, etc...)
    :return:
    '''
    def account(self, symbol, marginCoin):
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/account', params)
        else:
            return "pls check args"

    '''
    adjust leverage
    symbol: 合约交易对
    marginCoin: margin currency(ex. USDT, etc...)
    leverage: leverage
    holdSide: 持仓方向 long 多仓 short 空仓  全仓时可以不传
    :return:
    '''
    def leverage(self, symbol, marginCoin, leverage, holdSide=''):
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["leverage"] = leverage
            params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setLeverage', params)
        else:
            return "pls check args"

    '''
    adjust margin
    symbol: 合约交易对
    marginCoin: 保证金币种
    amount: Margin Amount Positive Increase Negative Decrease
    holdSide: 持仓方向 long 多仓 short 空仓  全仓时可以不传
    :return:
    '''
    def margin(self, symbol, marginCoin, amount, holdSide=''):
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["amount"] = amount
            params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMargin', params)
        else:
            return "pls check args"

    '''
    adjust margin mode
    symbol: 合约交易对
    marginCoin: 保证金币种
    marginMode: fixed = isolated  crossed = cross
    :return:
    '''
    def margin_mode(self, symbol, marginCoin, marginMode):
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["marginMode"] = marginMode
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMarginMode', params)
        else:
            return "pls check args"

    '''
    Set position mode
    symbol: 合约交易对
    marginCoin: 保证金币种
    holdMode: Position mode single_hold = single position double_hold = bidirectional position, default bidirectional
    :return:
    '''
    def position_mode(self, symbol, marginCoin, holdMode):
        params = {}
        if symbol and marginCoin and holdMode:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["holdMode"] = holdMode
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setPositionMode', params)
        else:
            return "pls check args"

    '''
    Query the number of openings
    symbol: 合约交易对
    marginCoin: 保证金币种
    openPrice： opening price
    openAmount: Opening quota
    leverage: Leverage default 20
    :return:
    '''
    def open_count(self, symbol, marginCoin, openPrice, openAmount, leverage=20):
        params = {}
        if symbol and marginCoin and openPrice and openAmount:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["openPrice"] = openPrice
            params["openAmount"] = openAmount
            params["leverage"] = leverage
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/open-count', params)
        else:
            return "pls check args"

    '''
    Get a list of account information
    productType: umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
    :return:
    '''
    def accounts(self, productType):
        params = {}
        if productType:
            params['productType'] = productType
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accounts', params)
        else:
            return "pls check args"

    '''
    Get a list of account flow information
    :return:
    '''
    def accountBill(self, symbol,marginCoin,startTime,endTime,lastEndId = '',pageSize=20,next=False):
        params = {}
        if symbol and marginCoin and startTime and endTime:
            params['symbol'] = symbol
            params['marginCoin'] = marginCoin
            params['startTime'] = startTime
            params['endTime'] = endTime
            params['lastEndId'] = lastEndId
            params['pageSize'] = pageSize
            params['next'] = next
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accountBill', params)
        else:
            return "pls check args"
