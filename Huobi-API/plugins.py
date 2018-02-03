#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-26 15:40:03
# @Author  : Polly
# @QQ      : 26716201


import sqlite3

def getDataFromDB(symbol, time_start, time_end, period):
	"""
		@ symbol: btcusdt, bchbtc, rcneth ... 
		@ time_start: 1min, 5min, 15min
		@ time_end: 1516884360 1516970700
		@ period: 1min, 5min, 15min
	"""
	result = {'price_open':[], 'price_close':[], 'price_low':[], 'price_high':[], 'price_avg':[], 'timestamp':[]}
	conn = sqlite3.connect('data.db')
	c = conn.cursor()    
	sql = "SELECT price_open, price_close, price_low, price_high, price_avg, timestamp  FROM huobi WHERE symbol='{}' AND period='{}' AND timestamp>{} AND timestamp<{} ORDER BY timestamp".format(symbol, period, time_start, time_end)
	c.execute(sql)
	data = c.fetchall()
	for d in data:
		result['price_open'].append(d[0])
		result['price_close'].append(d[1])
		result['price_low'].append(d[2])
		result['price_high'].append(d[3])
		result['price_avg'].append(d[4])
		result['timestamp'].append(d[5])
	conn.close()
	return result