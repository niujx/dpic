# -*- coding: utf-8 -*-
__author__ = 'yanshi'
from twisted.internet import reactor
from spiders.Spiders import DpicSpider
from scrapy import log, signals
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings

spider = DpicSpider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
#log.start(logfile='/home/yanshi/dpic_log/log', loglevel=log.DEBUG, logstdout=True)
log.start()
reactor.run()
log.msg("This is a warning")