# -*- coding: utf-8 -*-
__author__ = 'yanshi'
from pymongo import Connection
import re
import time, datetime
import random

ISOFMT = '%Y-%m-%d %X'
res = []
curtf = datetime.datetime(*time.strptime(time.strftime("2014-%m-24 %H:%M:%S"), ISOFMT)[:6])
for i in xrange(365):
    destf = curtf - datetime.timedelta(i)
    res.append(destf)
res.reverse()
print res
print random.choice(res)