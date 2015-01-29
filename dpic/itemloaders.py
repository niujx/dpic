# -*- coding: utf-8 -*-
__author__ = 'yanshi'
from scrapy.contrib.loader import ItemLoader


class ShopItemLoader(ItemLoader):
    def image_urls_in(self, values):
        for v in values:
            yield str(v).replace('249c249', '700x700')


    def comments_in(self, valus):
        for v in valus:
            yield unicode.strip(v)







