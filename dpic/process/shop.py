# -*- coding: utf-8 -*-
__author__ = 'yanshi'
from threading import Thread
from Queue import Queue, Empty
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
writer_queue = Queue()
flag = True
user_id = 10002
province_id = 19
source = 998


# select user_id from tbl_user_info where password='e10adc3949ba59abbe56e057f20f883e';

# random date
res = []
baseDate = datetime.datetime(*time.strptime(time.strftime("2015-%m-1 %H:%M:%S"), '%Y-%m-%d %X')[:6])
for i in xrange(90):
    res.append(baseDate - datetime.timedelta(i))
res.reverse()
print res
# random user_id
# conn = MySQLdb.connect(host='172.16.80.214', user='data', passwd='opensesame', db='ugc', charset='utf8')
# cursor = conn.cursor()
# cursor.execute(
#     "select user_id from tbl_user_info where password='e10adc3949ba59abbe56e057f20f883e' order by user_id  desc limit 1000")
# user_ids = []
# for user_id in cursor.fetchall():
#     user_ids.append(user_id[0])
#
# print user_ids


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
        for shop_info in db.shop_info.find({'$or': [{'image_paths': {'$exists': 1}}, {'comments': {'$exists': 1}}]},
                                           timeOut=False):
            queue.put(shop_info)
            # flag = False
        print 'all_done'


class Consumer(Thread):
    def run(self):
        global queue, flag, writer_queue
        while True:
            try:
                shop_info = queue.get()
            except Empty:
                break
            shop_id = long(shop_info['_id'])
            ugc_shop_info = ugc_db.shop.info.find_one({'_id': shop_id})
            try:
                city_id = ugc_shop_info['city_id']
            except Exception:
                # db.shop_info.update({'_id': shop_id}, {'$set': {'success': 2}})
                if ugc_shop_info is not None:
                    city_id = 1
                else:
                    print shop_id
                    continue

            try:
                for comment in shop_info['comments']:
                    self.add_comment(comment, shop_id, city_id)
            except Exception:
                pass

            try:
                for image_path in shop_info['image_paths']:
                    degrees = {}
                    name = find_image_name(image_path)
                    for code, image_id in ImageDegreeProcess().process(IMAGES_STORE + "/" + image_path):
                        degrees[str(code)] = str(image_id)
                    self.add_shop_image(degrees, name, shop_id, city_id)
            except Exception:
                pass

            ugc_db.shop.info.update({'_id': shop_id}, {'$set': {'dianping': 2}})
            db.shop_info.update({'_id': shop_id}, {'$set': {'success': 1}})
            print 'done'
            queue.task_done()


    def add_comment(self, context, shop_id, city_id):
        update_user_id = self.random_user_id()
        comment_obj = {'shop_id': shop_id, 'province_id': province_id,
                       'city_id': city_id,
                       'source': source, 'create_time': self.generator_date(), 'validate': 0, 'comment': context,
                       'hehe': 1}
        comment_id = ugc_db.comments.save(comment_obj)
        # self.to_sql(comment_id, 'comment_not_audit_info')
        ugc_db.user.ugc.update({'_id': update_user_id}, {'$set': {'dianping': 2}}, upsert=True)

    def add_shop_image(self, degrees, name, shop_id, city_id):
        update_user_id = self.random_user_id()
        image_obj = {'city_id': city_id, 'source': source, 'create_time': self.generator_date(), 'degree': degrees,
                     'image_name': name, 'province_id': province_id, 'shop_id': shop_id, 'validate': 0, 'hehe': 1}

        image_id = ugc_db.shop.image.save(image_obj)
        # self.to_sql(image_id, 'image_not_audit_info')
        ugc_db.user.ugc.update({'_id': update_user_id}, {'$set': {'dianping': 2}}, upsert=True)

    @staticmethod
    def generator_date():
        return random.choice(res)

    @staticmethod
    def to_sql(object_id, table_name):
        writer_queue.put((object_id, table_name))


class Write(Thread):
    def run(self):
        global writer_queue
        f = open('index.sql', 'a')
        while True:
            try:
                line = writer_queue.get(timeout=50)
                f.write(
                    "insert into %s (id,province_id,city_id,source) values ('%s',19,5,1);" % line)
                f.write('\n')
                writer_queue.task_done()
            except Empty:
                break
        f.close()


Product().start()
# Write().start()
for i in xrange(1, 50):
    Consumer(name=i).start()