# -*- coding: utf-8 -*-
__author__ = 'yanshi'
from threading import Thread
from Queue import Queue
from pymongo import MongoClient
from dpic.settings import DB_INFO, IMAGES_STORE, UGC_DB_INFO
from dpic.process.image import ImageDegreeProcess
import re
import time
import datetime
import random
import MySQLdb


db = MongoClient(host=DB_INFO.get('host'), port=DB_INFO.get('port')).dpic
ugc_db = MongoClient(host=UGC_DB_INFO.get('host'), port=UGC_DB_INFO.get('port')).ugc

queue = Queue(1000)
flag = True
user_id = 10002
province_id = 19
source = 998


# select user_id from tbl_user_info where password='e10adc3949ba59abbe56e057f20f883e';

# random date
res = []
baseDate = datetime.datetime(*time.strptime(time.strftime("2014-%m-24 %H:%M:%S"), '%Y-%m-%d %X')[:6])
for i in xrange(365):
    res.append(baseDate - datetime.timedelta(i))
res.reverse()

# random user_id
conn = MySQLdb.connect(host='172.16.80.214', user='data', passwd='opensesame', db='ugc', charset='utf8')
cursor = conn.cursor()
cursor.execute("select user_id from tbl_user_info where password='e10adc3949ba59abbe56e057f20f883e' order by user_id  desc limit 1000")
user_ids = []
for user_id in cursor.fetchall():
    user_ids.append(user_id[0])

print user_ids


def find_image_name(path):
    m = re.search('(?<=full/)(.*?)\.jpg', path, re.I)
    if m:
        return m.group(1)
    else:
        return 'none'


# e10adc3949ba59abbe56e057f20f883e

class Product(Thread):
    def run(self):
        global queue, flag
        for shop_info in db.shop_info.find({'image_paths': {'$exists': 1}}, timeOut=False):
            queue.put(shop_info)
            # flag = False
        print 'all_done'


class Consumer(Thread):
    def run(self):
        global queue, flag
        while flag:
            shop_info = queue.get()
            shop_id = long(shop_info['_id'])
            ugc_shop_info = ugc_db.shop.info.find_one({'_id': shop_id})
            try:
                city_id = ugc_shop_info['city_id']
            except TypeError:
                print shop_id
                continue

            for comment in shop_info['comments']:
                self.add_comment(comment, shop_id, city_id)

            for image_path in shop_info['image_paths']:
                degrees = {}
                name = find_image_name(image_path)
                for code, image_id in ImageDegreeProcess().process(IMAGES_STORE + "/" + image_path):
                    degrees[str(code)] = str(image_id)
                self.add_shop_image(degrees, name, shop_id, city_id)

            ugc_db.shop.info.update({'_id': shop_id}, {'$set': {'dianping': 2}})
            print 'done'
            queue.task_done()


    def add_comment(self, context, shop_id, city_id):
        comment_obj = {'shop_id': shop_id, 'user_id': self.random_user_id(), 'province_id': province_id,
                       'city_id': city_id,
                       'source': source, 'create_time': self.generator_date(), 'validate': 0, 'comment': context}

        ugc_db.comments.save(comment_obj)

    def add_shop_image(self, degrees, name, shop_id, city_id):
        image_obj = {'city_id': city_id, 'source': source, 'create_time': self.generator_date(), 'degree': degrees,
                     'image_name': name, 'province_id': province_id, 'shop_id': shop_id, 'validate': 0,
                     'user_id': self.random_user_id()}

        ugc_db.shop.image.save(image_obj)

    def generator_date(self):
        return random.choice(res)

    def random_user_id(self):
        return random.choice(user_ids)


Product().start()
for i in xrange(1, 20):
    Consumer(name=i).start()