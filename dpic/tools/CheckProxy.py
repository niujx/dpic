__author__ = 'yanshi'
import urllib2
import socket

for proxy in open('proxys', 'r'):
    opener = urllib2.build_opener(urllib2.ProxyHandler({'http': proxy}))
    urllib2.install_opener(opener)
    header = {'User-Agent':
                  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'}
    request = urllib2.Request('http://www.dianping.com/shop/17167447', headers=header)
    try:
        res = urllib2.urlopen(request, timeout=2)
        print res.code,proxy
    except Exception:
        pass






