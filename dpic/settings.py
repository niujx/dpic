# -*- coding: utf-8 -*-

# Scrapy settings for dpic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
# http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dpic'

SPIDER_MODULES = ['dpic.spiders']
NEWSPIDER_MODULE = 'dpic.spiders'

RETRY_ENABLED = False
COOKIES_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'dpic (+http://www.yourdomain.com)'

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

DOWNLOADER_MIDDLEWARES = {
    'middleware.ProxyMiddleware': 50,
    'middleware.RandomUserAgent': 100,
    'middleware.ErrorMonkeyMiddleware': 200,
}

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Host': 'www.dianping.com'
}

ITEM_PIPELINES = {
    'pipelines.ShopItemPipeline': 100
}

CONCURRENT_REQUESTS = 50

DB_INFO = {
    'host': '172.16.18.203',
    'port': 30000
}

UGC_DB_INFO = {
    'host': '172.16.80.121',
    'port': 30001
}

DOWNLOAD_DELAY = 0.5

LOG_PATH = '/home/yanshi/dpic_log/log'

HTTPERROR_ALLOWED_CODES = [404]

IMAGES_STORE = '/home/yanshi/dpic/image/1901'

# 图片处理接口
IMAGE_PROCESS_CALL = 'http://172.16.104.128:8015/picHandle'

IMAGE_UPLOAD = 'http://172.16.81.247:8180/traxexclouds/uploadimage.search'

# 代理
PROXYS = [
    'http://106.37.177.251:3128',
    'http://113.214.13.1:8000',
    'http://114.112.91.97:90',
    'http://114.255.183.163:8080',
    'http://114.255.183.174:8080',
    'http://115.236.59.194:3128',
    'http://115.239.210.199:80',
    'http://115.28.2.165:80',
    'http://115.29.247.115:8888',
    'http://116.228.55.217:8003',
    'http://116.236.216.116:8080',
    'http://117.177.240.43:80',
    'http://117.177.243.102:80',
    'http://117.177.243.107:80',
    'http://117.177.243.108:80',
    'http://117.177.243.14:80',
    'http://117.177.243.21:80',
    'http://117.177.243.22:80',
    'http://117.177.243.26:80',
    'http://117.177.243.30:80',
    'http://117.177.243.41:80',
    'http://117.177.243.42:80',
    'http://117.177.243.43:80',
    'http://117.177.243.46:80',
    'http://117.177.243.47:80',
    'http://117.177.243.53:80',
    'http://117.177.243.54:80',
    'http://117.177.243.67:80',
    'http://117.177.243.68:80',
    'http://117.177.243.69:80',
    'http://117.177.243.71:80',
    'http://117.177.243.75:80',
    'http://117.177.243.76:80',
    'http://117.177.243.77:80',
    'http://119.97.164.48:8085',
    'http://120.132.155.246:80',
    'http://120.198.243.113:80',
    'http://120.198.243.114:80',
    'http://120.198.243.116:80',
    'http://120.198.243.118:80',
    'http://120.198.243.14:80',
    'http://120.198.243.151:80',
    'http://120.198.243.15:80',
    'http://120.198.243.48:80',
    'http://120.198.243.50:80',
    'http://120.198.243.51:80',
    'http://120.198.243.52:80',
    'http://120.198.243.53:80',
    'http://120.198.243.54:80',
    'http://120.198.243.82:80',
    'http://120.198.243.83:80',
    'http://120.198.243.86:80',
    'http://122.136.46.151:3128',
    'http://122.96.59.106:80',
    'http://122.96.59.106:81',
    'http://122.96.59.106:82',
    'http://122.96.59.106:83',
    'http://122.96.59.106:843',
    'http://123.125.19.44:80',
    'http://125.46.19.92:808',
    'http://125.65.113.61:8080',
    'http://162.105.80.111:3128',
    'http://175.25.243.22:80',
    'http://180.180.121.237:80',
    'http://182.92.214.3:80',
    'http://183.136.152.26:80',
    'http://183.203.208.171:8118',
    'http://183.207.224.12:80',
    'http://183.207.224.14:80',
    'http://183.207.224.15:80',
    'http://183.207.224.42:80',
    'http://183.207.224.51:80',
    'http://183.207.224.51:82',
    'http://183.207.224.51:83',
    'http://183.207.224.51:84',
    'http://183.207.228.116:80',
    'http://183.207.228.117:80',
    'http://183.207.228.22:80',
    'http://183.207.228.58:80',
    'http://183.207.228.60:80',
    'http://183.207.228.7:80',
    'http://183.207.228.7:8000',
    'http://183.207.228.7:8080',
    'http://183.207.228.7:81',
    'http://183.207.228.7:82',
    'http://183.207.228.7:83',
    'http://183.207.228.7:84',
    'http://183.207.228.7:9000',
    'http://183.207.228.9:80',
    'http://183.207.228.9:82',
    'http://183.207.228.9:84',
    'http://183.207.228.9:87',
    'http://183.207.229.10:80',
    'http://183.207.229.10:81',
    'http://183.207.229.10:9000',
    'http://183.207.229.11:80',
    'http://183.207.229.12:80',
    'http://183.207.229.137:80',
    'http://183.207.229.13:80',
    'http://183.207.229.13:81',
    'http://183.207.229.138:80',
    'http://183.207.229.13:9000',
    'http://183.207.229.139:80',
    'http://183.207.232.193:8080',
    'http://183.207.232.194:8080',
    'http://183.207.237.11:80',
    'http://183.207.237.18:80',
    'http://183.207.237.18:81',
    'http://183.224.1.30:80',
    'http://202.106.16.36:3128',
    'http://202.106.169.228:8080',
    'http://202.107.233.85:8080',
    'http://210.101.131.231:8080',
    'http://218.204.140.212:8118',
    'http://218.206.83.89:80',
    'http://218.207.172.236:80',
    'http://218.240.131.12:80',
    'http://218.240.156.82:80',
    'http://218.4.236.117:80',
    'http://218.5.74.174:80',
    'http://218.59.144.120:80',
    'http://218.59.144.95:80',
    'http://218.84.189.41:1510',
    'http://219.239.90.83:80',
    'http://221.176.14.72:80',
    'http://222.161.248.122:80',
    'http://222.161.248.124:80',
    'http://222.45.196.19:8118',
    'http://222.87.129.218:80',
    'http://222.88.236.236:83',
    'http://27.145.145.105:8080',
    'http://58.251.78.71:8088',
    'http://60.190.51.178:808',
    'http://60.191.39.252:80',
    'http://60.194.14.144:82',
    'http://60.206.239.195:8118',
    'http://60.210.18.46:80',
    'http://61.143.158.226:808',
    'http://61.172.249.96:80',
    'http://61.184.192.42:80',
    'http://61.190.68.78:80',
    'http://61.53.143.179:80',
    'http://61.54.221.:3128',
]