# -*- coding: utf-8 -*-
import re

__author__ = 'yanshi'
from dpic.itemloaders import ShopItemLoader
from scrapy import Spider
from scrapy import log

from dpic.items import ShopItem
from dpic.settings import DB_INFO
from pymongo import MongoClient


class DpicSpider(Spider):
    name = "dianping"
    allowed_domains = ["dianping.com"]
    start_urls = [""]
    db = MongoClient(host=DB_INFO.get('host'), port=DB_INFO.get('port')).dpic

    def start_requests(self):
        shop_info_c = self.db.shop_info
        for shop_info in shop_info_c.find({'http_code': {'$ne': 404}}, timeout=False):
            yield self.make_requests_from_url(shop_info['url'])

    def parse(self, response):
        shop_url = response.url
        status = response.status
        log.msg(str(status) + ":" + str(shop_url), logLevel=log.INFO)

        if response.status == 404:
            self.db.shop_info.update({'url': shop_url}, {'$set': {'http_code': 404}})
            return

        m = re.search(r'shop/(\d+)', shop_url)
        if not m:
            return

        self.log(shop_url, level=log.INFO)
        l = ShopItemLoader(item=ShopItem(), response=response)
        l.add_xpath('comments', '//div[@class="content"]/p[@class="desc"]/text()')
        l.add_xpath('image_urls', '//div[@class="content"]//img/@data-lazyload')
        l.add_value('shop_id', m.group(1))
        l.add_value('shop_url', shop_url)
        return l.load_item()











