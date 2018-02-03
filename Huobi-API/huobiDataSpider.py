#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-26 15:40:03
# @Author  : Polly
# @QQ      : 26716201


from HuobiService import *
from sqlalchemy import *
from sqlalchemy.orm import *
from db_models import *
from db_config import DB_CONFIG
import time





class HuobiDataSpider(object):
	"""docstring for IsIsTopoGenerator"""
	def __init__(self):
		self.usdt_list = ["usdt", "btc", "bch", "xrp", "eth", "ltc", "dash", "eos", "etc", "omg", "zec", "elf", "smt", "iost", "ven", "qtum", "neo", "hsr", "cvc", "storj", "gnt", "snt"]
		self.btc_list = ["btc", "bch", "xrp", "eth", "ltc", "dash", "eos", "etc", "omg", "zec", "zil", "soc", "mee", "eko", "link", "qtum", "elf", "ven", "adx", "evx", "utk", "dta"]
		self.eth_list = ["eth", "eos","omg", "zil", "soc", "mee", "eko", "link", "iost", "elf", "dta", "adx", "evx", "utk", "let"]
		
	def connectDB(self, DB_CONFIG):
		try:
			engine = create_engine('{engine}://{username}:{password}@{address}:{port}/{database}?charset=utf8'.format(**DB_CONFIG), echo=False)
			DB_Session = sessionmaker(bind=engine)
			self.session = DB_Session()
			print "DataBase connect successful!"
		except:
			print "DataBase connect failed..."

	def disconnectDB(self):
		try:
			self.session.commit()
			self.session.close()
			print "DataBase disconnect successful!"
		except:
			print "DataBase disconnect failed..."

	def getSymbolListFromHuobi(self):
		symbol_list = get_symbols().get("data", [])
		return map(lambda x:x['base-currency']+x['quote-currency'], symbol_list)

	def getKlineDataFromHuobi(self, symbol_list, period, size=1):
		result = []
		for i in symbol_list:
			r = get_kline(symbol, period, size)
			data_list = r.get("data", [])
			for d in data_list:
				price_avg = d['close'] if d['vol']==0.0 else d['vol']/d['amount']
				item = (symbol, period, d['amount'], d['count'], d['open'], \
					d['close'], d['low'], d['high'], d['vol'], price_avg, d['id'])
				result.append(item)
		return result

	def getDataFromKline(self, symbol_list, period, size=1):
		result = []
		for i in symbol_list[1:]:
			symbol = i + symbol_list[0]
			r = get_kline(symbol, period, size)
			data_list = r.get("data", [])
			for d in data_list:
				price_avg = d['close'] if d['vol']==0.0 else d['vol']/d['amount']
				item = (symbol, period, d['amount'], d['count'], d['open'], \
					d['close'], d['low'], d['high'], d['vol'], price_avg, d['id'])
				result.append(item)
		return result

	def storageDataToDB(self, period):
		print "Start Getting Data[{}]..".format(period)
		symbol_list = self.getSymbolListFromHuobi()
		while True:
			start = time.time()
			count = 0
			# data_list = self.getDataFromKline(self.usdt_list, period, 1)
			# data_list.extend(self.getDataFromKline(self.btc_list, period, 1))
			# data_list.extend(self.getDataFromKline(self.eth_list, period, 1))
			data_list = self.getKlineDataFromHuobi(symbol_list, period, 1)
			for d in data_list:
				h = Huobi(symbol=d[0], period=d[1], amount=d[2], count=d[3], price_open=d[4], price_close=d[5],\
					price_low=d[6], price_high=d[7], vol=d[8], price_avg=d[9], timestamp=d[10])
				self.session.add(h)
				self.session.commit()
			count = len(data_list)
			end = time.time()
			cost = end-start
			rest = int(period.split('m')[0])*60-int(cost)
			rest = rest if rest>0 else 1
			print "Getted {} Data[{}] Success, Time Cost {}s, Sleep {}s".format(count, period, cost, rest)
			time.sleep(rest)
		self.disconnectDB()

def test():
	h = HuobiDataSpider()
	h.connectDB(DB_CONFIG)
	h.storageDataToDB('1min')











