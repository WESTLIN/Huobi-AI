#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-26 15:40:03
# @Author  : Polly
# @QQ      : 26716201


from threading import Timer
from HuobiService import *
import sqlite3, time, sched

def initDB():
	conn = sqlite3.connect('data.db')
	print "Opened database successfully"
	c = conn.cursor()
	c.execute('''CREATE TABLE huobi
		(id INTEGER PRIMARY KEY AUTOINCREMENT,
		symbol CHAR(20) NOT NULL,
		period CHAR(10) NOT NULL,
		timestamp TEXT NOT NULL,
		price FLOAT NOT NULL)''')
	print "Table created successfully";
	conn.commit()
	conn.close()

if __name__ == '__main__':
	initDB()
	