#!/usr/bin/python

from ..client import Client
from ..consts import *


class PlanApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    '''
    Plan to place an order
    triggerPrice: trigger price
    executePrice: strike price
    triggerType: Trigger type fill_price market_price
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
    def place_plan(self, symbol, marginCoin, size, side, orderType, triggerPrice, triggerType, executePrice='', clientOrderId='', timeInForceValue='normal', presetTakeProfitPrice='', presetStopLossPrice=''):
        params = {}
        if symbol and marginCoin and side and orderType and triggerPrice and triggerType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["triggerPrice"] = triggerPrice
            params["executePrice"] = executePrice
            params["triggerType"] = triggerType
            params["size"] = size
            params["side"] = side
            params["orderType"] = orderType
            params["timeInForceValue"] = timeInForceValue
            params["clientOrderId"] = clientOrderId
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placePlan', params)
        else:
            return "pls check args "

    '''
    Modify plan delegation
    triggerPrice: trigger price
    executePrice: strike price
    triggerType: Trigger type fill_price market_price
    marginCoin: Margin currency
    orderType: limit (limit price) market (market price)
    :return:
    '''
    def modify_plan(self, symbol, marginCoin, orderId, orderType, triggerPrice, triggerType, executePrice=''):
        params = {}
        if symbol and marginCoin and orderType and orderId and triggerType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            params["triggerPrice"] = triggerPrice
            params["executePrice"] = executePrice
            params["triggerType"] = triggerType
            params["orderType"] = orderType
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyPlan', params)
        else:
            return "pls check args "

    '''
    Modify the plan order to preset take profit and stop loss
    orderId：order number
    triggerType: trigger type
    marginCoin: Margin currency
    planType: Plan order type normal_plan Normal plan profit_plan Stop profit plan loss_plan Stop loss plan
    presetTakeProfitPrice: Default Take Profit Price
    presetStopLossPrice： Preset stop loss price
    :return:
    '''
    def modify_plan_preset(self, symbol, marginCoin, orderId, planType='normal_plan', presetTakeProfitPrice='', presetStopLossPrice=''):
        params = {}
        if symbol and marginCoin and orderId and planType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["planType"] = planType
            params["orderId"] = orderId
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyPlanPreset', params)
        else:
            return "pls check args "

    '''
    Modify the plan order to preset take profit and stop loss
    orderId：order number
    triggerPrice: trigger price
    marginCoin: Margin currency
    :return:
    '''
    def modify_tpsl_plan(self, symbol, marginCoin, orderId, triggerPrice ):
        params = {}
        if symbol and marginCoin and orderId and triggerPrice:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            params["triggerPrice"] = triggerPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyTPSLPlan', params)
        else:
            return "pls check args "

    '''
    Take Profit and Stop Loss
    Currently, take profit and stop loss orders are only supported at market prices. The trigger type is transaction price.
    symbol: trading pair name
    marginCoin: Margin currency
    orderId: order id
    planType: Order Type profit_plan Take Profit Plan loss_plan Stop Loss Plan
    holdSide: Position direction long long position short short position
    :return:
    '''
    def place_tpsl(self, symbol, marginCoin, triggerPrice, planType, holdSide ):
        params = {}
        if symbol and marginCoin and planType and holdSide and triggerPrice:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["planType"] = planType
            params["holdSide"] = holdSide
            params["triggerPrice"] = triggerPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placeTPSL', params)
        else:
            return "pls check args "


    '''
    Plan order (take profit and stop loss) to cancel the order
    symbol: trading pair name
    marginCoin: Margin currency
    orderId: order id
    planType: order type normal_plan plan commission profit_plan take profit plan loss_plan stop loss plan
    :return:
    '''
    def cancel_plan(self, symbol, marginCoin, orderId, planType):
        params = {}
        if symbol and marginCoin and planType and orderId:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["planType"] = planType
            params["orderId"] = orderId
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/cancelPlan', params)
        else:
            return "pls check args "

    '''
    Get current plan delegation
    isPlan: Whether to query plan commission plan plan commission profit_loss stop profit stop loss
    :return:
    '''
    def current_plan(self, symbol, isPlan='plan'):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["isPlan"] = isPlan
            return self._request_with_params(GET, MIX_PLAN_V1_URL + '/currentPlan', params)
        else:
            return "pls check args "

    '''
    Get historical planning orders
    isPre： Whether to query the previous page
    isPlan: Whether to query plan commission plan plan commission profit_loss stop profit stop loss
    :return:
    '''
    def history_plan(self, symbol, startTime, endTime, pageSize, lastEndId='', isPre=False, isPlan='plan'):
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["isPre"] = isPre
            params["isPlan"] = isPlan
            return self._request_with_params(GET, MIX_PLAN_V1_URL + '/historyPlan', params)
        else:
            return "pls check args "
