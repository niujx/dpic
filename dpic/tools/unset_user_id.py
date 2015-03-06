# -*- coding: utf-8 -*-
from bson import ObjectId

__author__ = 'yanshi'
from pymongo import MongoClient, Connection

db = MongoClient(host='172.16.80.121', port=30001).ugc
for id in open('/home/yanshi/PycharmProjects/dpic/dpic/process/index.sql', 'r'):
    _id = ObjectId(str(id).strip())
    db.shop.image.update({'_id': _id}, {'$unset': {'user_id': 1}})
