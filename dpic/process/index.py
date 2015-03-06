__author__ = 'yanshi'
from pymongo import MongoClient
from dpic.settings import UGC_DB_INFO

ugc_db = MongoClient(host=UGC_DB_INFO.get('host'), port=UGC_DB_INFO.get('port')).ugc

for comment in ugc_db.comments.find({'source': 998}, {'_id': 1, 'province_id': 1, 'city_id': 1}, timeOut=False):
    print comment
    f = open('index.sql', 'a')
    f.write('''insert into comment_not_audit_info (id,province_id,city_id,source) values ('%s',%d,%d,998);''' % (
        comment['_id'], comment['province_id'], comment['city_id']))
    f.write('\n')

for image in ugc_db.shop.image.find({'source': 998}, {'_id': 1, 'province_id': 1, 'city_id': 1}, timeOut=False):
    print image
    f = open('index.sql', 'a')
    f.write('''insert into image_not_audit_info (id,province_id,city_id,source) values ('%s',%d,%d,998);''' % (
        image['_id'], image['province_id'], image['city_id']))
    f.write('\n')

