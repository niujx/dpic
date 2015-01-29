# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log, Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
from pymongo import MongoClient
from dpic.settings import DB_INFO

import re


def host(image_url):
    match = re.search(r'//(.*?)/', image_url)
    if match:
        return match.group(1)


class ShopItemPipeline(ImagesPipeline):
    db = MongoClient(host=DB_INFO.get('host'), port=DB_INFO.get('port')).dpic

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, headers={'host': host(image_url)})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        self.save_db(item)
        return item

    def save_db(self, item):
        log.msg(item, log.INFO)
        collection = self.db.shop_info
        collection.update({'url': item.get('shop_url')[0]},
                          {'$set': {'comments': item.get('comments'), 'image_paths': item.get('image_paths')}}, True,
                          True)
        return item


if __name__ == '__main__':
    m = re.search(r'//(.*?)/', 'http://i2.s1.dpfile.com/pc/daa0602b9e3134cddfd59f81ba6846ee(700x700)/thumb.jpg')
    if m:
        print m.group(1)
