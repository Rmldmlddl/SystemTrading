#!/usr/bin/python

from ..client import Client
from ..consts import *


class MarketApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    '''
    Get contract list
    productType: umcbl  (USDT professional contract) 
                 dmcbl  (mixed contract)
                 sumcbl (USDT professional contract simulation disk) 
                 sdmcbl (mixed contract simulation disk)
    :return:
    '''
    def contracts(self, productType):
        params = {}
        if productType:
            params['productType'] = productType
        return self._request_with_params(GET, MIX_MARKET_V1_URL + '/contracts', params)

    '''
    Get depth data
    symbol：合约交易对
    :return:
    '''
    def depth(self, symbol, limit='150'):
        params = {}
        if symbol and limit and type:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/depth', params)
        else:
            return "pls check args"

    '''
    Get ticker information based on currency pair
    symbol：合约交易对
    :return:
    '''
    def ticker(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/ticker', params)
        else:
            return "pls check args"

    '''
    Get all ticker information
    productType: umcbl  (USDT professional contract) 
                 dmcbl  (mixed contract)
                 sumcbl (USDT professional contract simulation disk) 
                 sdmcbl (mixed contract simulation disk)
    :return:
    '''
    def tickers(self,productType):
        params = {}
        if productType:
            params['productType'] = productType
        return self._request_with_params(GET, MIX_MARKET_V1_URL + '/tickers', params)

    '''
    Get real-time deals
    symbol：合约交易对
    :return:
    '''
    def fills(self, symbol, limit=100):
        params = {}
        if symbol and limit:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/fills', params)
        else:
            return "pls check args"

    '''
    Get k-line information
    params
    period: 60, 300, 900, 1800, 3600,14400,43200, 86400, 604800(sec)
    startTime: Starting time
    endTime: End Time
    :return:
    '''
    def candles(self, symbol, granularity, startTime='', endTime=''):
        params = {}
        if symbol and granularity:
            params["symbol"] = symbol
            params["granularity"] = granularity
            params["startTime"] = startTime
            params["endTime"] = endTime
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/candles', params)
        else:
            return "pls check args"

    '''
    Currency Index Price
    symbol：合约交易对
    :return:
    '''
    def index(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/index', params)
        else:
            return "pls check args"

    '''
    next billing time
    symbol：合约交易对
    :return:
    '''
    def funding_time(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/funding-time', params)
        else:
            return "pls check args"

    '''
    contract mark price
    symbol：合约交易对
    :return:
    '''
    def market_price(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/mark-price', params)
        else:
            return "pls check args"

    '''
    Historical Funding Rate
    symbol：合约交易对
    pageSize: Number of queries
    pageNo: Query pages
    nextPage: Whether to query the next page
    :return:F
    '''
    def history_fund_rate(self, symbol, pageSize=20, pageNo=1, nextPage=False):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            params["nextPage"] = nextPage
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/history-fundRate', params)
        else:
            return "pls check args"

    '''
    
Current funding rate
    symbol：合约交易对
    :return:F
    '''
    def current_fund_rate(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/current-fundRate', params)
        else:
            return "pls check args"

    '''
    Get the total open interest of the platform
    symbol：合约交易对
    :return:
    '''
    def open_interest(self, symbol):
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/open-interest', params)
        else:
            return "pls check args"
