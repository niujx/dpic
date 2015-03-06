__author__ = 'yanshi'
from pymongo import Connection
import re

db = Connection(host='172.16.18.203', port=30000).dpic
for line in open(r'/home/yanshi/info_1901_new', 'r'):
    vals = line.split(',')
    m = re.search('(http://www.dianping.com/shop/\d+)', vals[1], re.I)
    if m:
        url = m.group(1)

    print vals[0].strip(), url.strip()
    db.shop_info.save({'_id': int(vals[0].strip()), 'url': url.strip()})

