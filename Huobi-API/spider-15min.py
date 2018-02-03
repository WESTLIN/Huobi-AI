#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-26 15:40:03
# @Author  : Polly
# @QQ      : 26716201

from huobiDataSpider import HuobiDataSpider
from db_config import DB_CONFIG


if __name__ == '__main__':
	h = HuobiDataSpider()
	h.connectDB(DB_CONFIG)
	h.storageDataToDB('15min')