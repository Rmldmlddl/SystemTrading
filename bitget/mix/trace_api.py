#!/usr/bin/python

from ..client import Client
from ..consts import *


class TraceApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    '''
    Trader closes position
    symbol： trading pair name
    trackingNo: track order number
    :return:
    '''

    def close_track_order(self, symbol, trackingNo):
        params = {}
        if symbol and trackingNo:
            params["symbol"] = symbol
            params["trackingNo"] = trackingNo
            return self._request_with_params(POST, MIX_TRACE_V1_URL + '/closeTrackOrder', params)
        else:
            return "pls check args "

    '''
    The trader gets the current order
    symbol: trading pair name
    productType: umcbl (USDT professional contract)
                 dmcbl (mixed contract) 
                 sumcbl (USDT professional contract simulation disk) 
                 sdmcbl (mixed contract simulation disk)
    pageNo： start from 1
    :return:
    '''

    def current_track(self, symbol, productType, pageSize=20, pageNo=1):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["productType"] = productType
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/currentTrack', params)
        else:
            return "pls check args "

    '''
    The trader gets the current order
    symbol: trading pair name
    startTime: Starting time
    endTime: End Time
    pageSize: Number of queries
    pageNo: Query pages
    :return:
    '''

    def history_track(self, startTime, endTime, pageSize=100, pageNo=1):
        params = {}
        if startTime and endTime:
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/historyTrack', params)
        else:
            return "pls check args "

    '''
    Trader's Profit Distribution Summary
    :return:
    '''

    def summary(self):
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/summary')

    '''
    Trader's profit distribution summary (by settlement currency)
    :return:
    '''

    def profit_settle_margin_coin(self):
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/profitSettleTokenIdGroup')

    '''
    Trader's Profit Distribution Summary (by date)
    :return:
    '''

    def profit_date_group(self, pageSize, pageNo):
        params = {}
        if pageSize and pageNo:
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/profitDateGroupList', params)
        else:
            return "pls check args "

    '''
    Trader's historical profit distribution details
    :return:
    '''

    def profit_date_detail(self, marginCoin, date, pageSize, pageNo):
        params = {}
        if marginCoin and date and pageSize and pageNo:
            params["marginCoin"] = marginCoin
            params["date"] = date
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/profitDateList', params)
        else:
            return "pls check args "

    '''
    Trader's Pending Profit Details
    :return:
    '''

    def wait_profit_detail(self, pageSize, pageNo):
        params = {}
        if pageSize and pageNo:
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/waitProfitDateList', params)
        else:
            return "pls check args "

    '''
    Follower Get information on opening and closing orders
    :return:
    '''

    def follower_history_orders(self, page_size, page_no, start_time, end_time):
        params = {}
        if page_size and page_no:
            params["pageSize"] = page_size
            params["pageNo"] = page_no

        if start_time and end_time:
            params["startTime"] = start_time
            params["endTime"] = end_time

        return self._request_with_params(GET, MIX_TRACE_V1_URL + '/followerHistoryOrders', params)
