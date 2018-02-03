#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################
#    getDataFromDB(symbol, time_start, time_end, period)        #
#        @ symbol: btcusdt, bchbtc, rcneth ...                  #
#        @ time_start: more than 1516884360                     #
#        @ time_end: less than 1516970700                       #
#        @ period: 1min, 5min, 15min                            #
#    --------------------------------------------------         #
#      return a dict:                                           #
#        {'price_open':[...],   'price_close':[...]             #
#         'price_low':[...],    'price_high':[...]              #
#         'price_avg':[...],    'timestamp':[...]}              #
#################################################################

from plugins import getDataFromDB

if __name__ == '__main__':
	r = getDataFromDB("btcusdt", 0, 9999999999, '1min')
	print r