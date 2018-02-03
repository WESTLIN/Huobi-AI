#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-26 15:40:03
# @Author  : Polly
# @QQ      : 26716201


from threading import Timer
from HuobiService import *
import sqlite3, time, sched

schedule = sched.scheduler(time.time, time.sleep)  

period_list = ['1min', '5min', '15min']

usdt_list = ["usdt", "btc", "bch", "xrp", "eth", "ltc", "dash", "eos", "etc", "omg", "zec", "elf", "smt", "iost", "ven", "qtum", "neo", "hsr", "cvc", "storj", "gnt", "snt"]
btc_list = ["btc", "bch", "xrp", "eth", "ltc", "dash", "eos", "etc", "omg", "zec", "zil", "soc", "mee", "eko", "link", "qtum", "elf", "ven", "adx", "evx", "utk", "dta"]
eth_list = ["eth", "eos","omg", "zil", "soc", "mee", "eko", "link", "iost", "elf", "dta", "adx", "evx", "utk", "let"]
# symbol_list = [usdt_list, btc_list, eth_list]
size_list = [60, 12, 4]


def initDB():
	conn = sqlite3.connect('data.db')
	print "Opened database successfully"
	c = conn.cursor()
	c.execute('''CREATE TABLE huobi (
		id          INTEGER   PRIMARY KEY AUTOINCREMENT,
		symbol      CHAR (20) NOT NULL,
		period      CHAR (10) NOT NULL,
		amount      INT       NOT NULL,
		count       INT       NOT NULL,
		price_open  DOUBLE    NOT NULL,
		price_close DOUBLE    NOT NULL,
		price_low   DOUBLE    NOT NULL,
		price_high  DOUBLE    NOT NULL,
		vol         DOUBLE    NOT NULL,
		price_avg   DOUBLE    NOT NULL,
		timestamp   INTEGER   NOT NULL
	)''')
	print "Table created successfully";
	conn.commit()
	conn.close()

def getDataFromKline(symbol_list, period, size):
	result = []
	for i in symbol_list[1:]:
		symbol = i + symbol_list[0]
		r = get_kline(symbol, period, size)
		data_list = r.get("data", [])
		for d in data_list:
			print d
			price_avg = d['close'] if d['vol']==0.0 else d['vol']/d['amount']
			# price = 0.0 if d['vol']==0.0 else d['vol']/(d['amount']*d['count'])
			# timestamp = d['id']
			item = (symbol, period, d['amount'], d['count'], d['open'], \
				d['close'], d['low'], d['high'], d['vol'], price_avg, d['id'])
			result.append(item)
	return result

def get1minDataFromHuobi():
	while True:
		start = time.time()
		count = 0
		conn = sqlite3.connect('data.db')
		c = conn.cursor()
		data_list = getDataFromKline(usdt_list, "1min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		data_list = getDataFromKline(btc_list, "1min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		data_list = getDataFromKline(eth_list, "1min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		conn.commit()
		conn.close()
		end = time.time()
		cost = end-start
		rest = 60-int(cost)
		print "Get {} Data[{}] Success, Time Cost {}s, Sleep {}s".format(count, "1min", end-start, rest)
		time.sleep(60-rest)

def get5minDataFromHuobi():
	while True:
		start = time.time()
		count = 0
		conn = sqlite3.connect('data.db')
		c = conn.cursor()
		data_list = getDataFromKline(usdt_list, "5min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		data_list = getDataFromKline(btc_list, "5min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		data_list = getDataFromKline(eth_list, "5min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		conn.commit()
		conn.close()
		end = time.time()
		cost = end-start
		rest = 60-int(cost)
		print "Get {} Data[{}] Success, Time Cost {}s, Sleep {}s".format(count, "5min", end-start, rest)
		time.sleep(300-rest)

def get15minDataFromHuobi():
	while True:
		start = time.time()
		count = 0
		conn = sqlite3.connect('data.db')
		c = conn.cursor()
		data_list = getDataFromKline(usdt_list, "15min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		data_list = getDataFromKline(btc_list, "15min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		data_list = getDataFromKline(eth_list, "15min", 1)
		c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
		count += len(data_list)
		conn.commit()
		conn.close()
		end = time.time()
		cost = end-start
		rest = 60-int(cost)
		print "Get {} Data[{}] Success, Time Cost {}s, Sleep {}s".format(count, "15min", end-start, rest)
		time.sleep(900-rest)

if __name__ == '__main__':
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	data_list = getDataFromKline(usdt_list, '1min', 1440)
	c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
	data_list = getDataFromKline(usdt_list, '5min', 288)
	c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
	data_list = getDataFromKline(usdt_list, '15min', 96)
	c.executemany('INSERT INTO huobi (symbol, period, amount, count, price_open, price_close, price_low, price_high, vol, price_avg, timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)', data_list)
	conn.commit()
	conn.close()
	
	


'''
    for i in usdt_list:
        try:
            filename = "USDT/{}.json".format(i)
            with open(filename, "w") as f:
                name = i+"usdt"
                result = get_kline(name, "1min", 2000)
                if type(result)==dict:
                    result = json.dumps(result, indent=4)
                f.write(result)
                print "File:[{}] write success!".format(filename)
        except Exception, e:
            print "Error:{}-{}".format(Exception, e)
            continue
    print "-------------------------"
    for i in btc_list:
        try:
            filename = "BTC/{}.json".format(i)
            with open(filename, "w") as f:
                name = i+"btc"
                result = get_kline(name, "1min", 2000)
                if type(result)==dict:
                    result = json.dumps(result, indent=4)
                f.write(result)
                print "File:[{}] write success!".format(filename)
        except Exception, e:
            print "Error:{}-{}".format(Exception, e)
            continue
    print "-------------------------"
    for i in eth_list:
        try:
            filename = "ETH/{}.json".format(i)
            with open(filename, "w") as f:
                name = i+"eth"
                result = get_kline(name, "1min", 2000)
                # print type(result)
                if type(result)==dict:
                    result = json.dumps(result, indent=4)
                f.write(result)
                print "File:[{}] write success!".format(filename)
        except Exception, e:
            print "Error:{}-{}".format(Exception, e)
            continue
'''