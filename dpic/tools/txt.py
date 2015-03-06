# -*- coding: utf-8 -*-
__author__ = 'yanshi'
from pymongo import MongoClient

client = MongoClient(host='172.16.18.203', port=30000)
ugc = client.ugc
print ugc.yanshi.test.save({'name': 'yanshi'})