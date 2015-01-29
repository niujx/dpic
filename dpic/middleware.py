# -*- coding: utf-8 -*-
__author__ = 'yanshi'
import random
import Queue
from scrapy.exceptions import IgnoreRequest
from scrapy import log
from dpic.settings import PROXYS


class RandomUserAgent():
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist("USER_AGENTS"))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))
        log.msg(request.meta['proxy'], logLevel=log.INFO)


class ProxyMiddleware(object):
    def __init__(self):
        self.proxys = Queue.Queue()
        for proxy in PROXYS:
            self.proxys.put(proxy)

    def process_request(self, request, spider):
        if self.proxys.qsize() > 0:
            request.meta['proxy'] = self.proxys.get()
        log.msg(self.proxys.qsize(), logLevel=log.INFO)

    def process_response(self, request, response, spider):
        log.msg(request.meta['proxy'], logLevel=log.INFO)
        self.proxys.put(request.meta['proxy'])
        return response

    def process_exception(self, request, exception, spider):
        self.proxys.put(request.meta['proxy'])


class ErrorMonkeyMiddleware(object):
    def process_request(self, request, spider):
        if 'x-ignore-request' in request.url:
            raise IgnoreRequest()
        elif 'x-error-request' in request.url:
            _ = 1 / 0

    def process_response(self, request, response, spider):
        if 'x-ignore-response' in request.url:
            raise IgnoreRequest()
        elif 'x-error-response' in request.url:
            _ = 1 / 0
        else:
            return response

